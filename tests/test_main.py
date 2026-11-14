import io
import json
import logging
import os
import sqlite3
import tempfile
import unittest
from datetime import datetime, timezone
from unittest.mock import Mock, patch

import pandas as pd
import requests

import main
import update_readme

KEY = 'a1b2c3d4' * 4
HEADER = b'latitude,longitude,bright_ti4,acq_date,acq_time,confidence,frp,daynight\n'


def rows(*points):
    return pd.DataFrame(
        [{'latitude': lat, 'longitude': lon, 'acq_date': date, 'acq_time': 1030} for lat, lon, date in points]
    )


class SecretTests(unittest.TestCase):
    def test_every_log_record_is_masked(self):
        logger = logging.getLogger('secret-test')
        stream_records = []

        class Capture(logging.Handler):
            def emit(self, record):
                stream_records.append(record.getMessage())

        handler = Capture()
        handler.addFilter(main.SecretFilter())
        logger.addHandler(handler)
        logger.propagate = False
        error = requests.ConnectionError(f'Max retries exceeded with url: /api/area/csv/{KEY}/MODIS/1')
        logger.error('hata: %s', error)

        self.assertEqual(len(stream_records), 1)
        self.assertNotIn(KEY, stream_records[0])
        self.assertIn('[REDACTED]', stream_records[0])

    def test_logging_writes_no_file(self):
        root = logging.getLogger()
        saved = root.handlers[:]
        try:
            main.configure_logging()
            self.assertFalse([h for h in root.handlers if isinstance(h, logging.FileHandler)])
        finally:
            root.handlers[:] = saved

    def test_empty_secret_is_not_selected(self):
        env = {f'MAP_KEY_{i}': '' for i in range(1, 8)}
        env['MAP_KEY_3'] = KEY
        with patch.dict(os.environ, env, clear=True):
            self.assertEqual(main.select_map_key(), KEY)

    def test_no_secret_stops_the_run(self):
        with patch.dict(os.environ, {}, clear=True), self.assertRaises(SystemExit):
            main.select_map_key()


class DataRuleTests(unittest.TestCase):
    def test_border_keeps_turkey_and_drops_neighbours(self):
        inside = [(36.20, 36.16), (37.03, 27.43), (38.32, 26.30), (40.16, 25.85), (42.02, 35.15), (37.25, 42.47)]
        outside = [(35.88, 36.50), (39.10, 26.33), (36.20, 37.13), (37.05, 41.21), (41.64, 41.64), (40.85, 25.87)]
        data = rows(*[(lat, lon, '2026-11-02') for lat, lon in inside + outside])

        result = main.in_turkey(data)

        self.assertEqual(result.tolist(), [True] * len(inside) + [False] * len(outside))

    def test_request_covers_yesterday(self):
        self.assertGreaterEqual(main.DAY_RANGE, 2)

    def test_last_24_hours(self):
        now = datetime(2026, 11, 2, 3, 30, tzinfo=timezone.utc)
        data = pd.DataFrame({
            'acq_date': ['2026-11-02', '2026-11-01', '2026-11-01'],
            'acq_time': [8, 331, 329],
            'value': ['keep', 'keep', 'drop'],
        })

        self.assertEqual(list(main.last_24_hours(data, now=now)['value']), ['keep', 'keep'])

    def test_api_text_response_is_rejected(self):
        response = Mock(content=b'Invalid MAP_KEY.', raise_for_status=Mock())
        with patch('main.requests.get', return_value=response), self.assertRaises(ValueError):
            main.fetch_satellite(KEY, 'VIIRS_SNPP_NRT')

    def test_requests_use_timeout(self):
        response = Mock(content=HEADER, raise_for_status=Mock())
        with patch('main.requests.get', return_value=response) as get:
            main.fetch_satellite(KEY, 'VIIRS_SNPP_NRT')

        self.assertEqual(get.call_args.kwargs['timeout'], main.REQUEST_TIMEOUT)

    def test_archive_removes_bbox_era_foreign_rows_only(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, 'archive.csv')
            rows((36.20, 37.13, '2025-07-01'), (36.20, 37.13, '2026-03-01'), (37.03, 27.43, '2026-03-01')).to_csv(
                path, index=False
            )
            main.update_archive(path, rows((39.0, 33.0, '2026-11-02')))
            result = pd.read_csv(path)

        self.assertEqual(len(result), 3)
        self.assertEqual(result['acq_date'].tolist(), ['2025-07-01', '2026-03-01', '2026-11-02'])

    def test_archive_ignores_refetched_rows(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, 'archive.csv')
            data = rows((39.0, 33.0, '2026-11-02'))
            main.update_archive(path, data)
            main.update_archive(path, data)

            self.assertEqual(len(pd.read_csv(path)), 1)

    def test_empty_response_keeps_archive(self):
        empty = pd.read_csv(io.BytesIO(HEADER))
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, 'archive.csv')
            rows((39.0, 33.0, '2026-11-02')).to_csv(path, index=False)
            main.update_archive(path, empty)

            self.assertEqual(len(pd.read_csv(path)), 1)

    def test_empty_source_keeps_numeric_columns(self):
        empty = pd.read_csv(io.BytesIO(HEADER))
        combined = main.concat_non_empty([rows((39.0, 33.0, '2026-11-02')), empty])

        self.assertEqual(len(combined), 1)
        self.assertTrue(pd.api.types.is_float_dtype(combined['latitude']))
        self.assertIs(main.concat_non_empty([empty, empty]), empty)

    def test_database_is_compacted(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, 'fire.db')
            big = pd.DataFrame({'latitude': [39.0] * 50000, 'longitude': [33.0] * 50000})
            main.update_database(path, big)
            main.update_database(path, big.head(1))
            with sqlite3.connect(path) as conn:
                free_pages = conn.execute('pragma freelist_count').fetchone()[0]
                count = conn.execute('select count(*) from fire_data').fetchone()[0]

        self.assertEqual(free_pages, 0)
        self.assertEqual(count, 1)


class ReadmeTests(unittest.TestCase):
    NOW = datetime(2026, 11, 2, 12, 0)

    def write_archive(self, folder, csv_text):
        path = os.path.join(folder, 'TUR_TEST.csv')
        with open(path, 'wb') as f:
            f.write(csv_text)
        return os.path.join(folder, '*.csv')

    def test_empty_window_replaces_old_table(self):
        with tempfile.TemporaryDirectory() as folder:
            old = HEADER + b'39.0,33.0,310.0,2026-10-01,1030,n,4.0,D\n'
            recent = update_readme.load_last_24_hours(self.NOW, self.write_archive(folder, old))

        text = update_readme.build_readme(recent, self.NOW)

        self.assertIn('tespit edilmedi', text)
        self.assertNotIn('2026-10-01', text)
        self.assertIn('2026-11-02 12:00:00', text)

    def test_newest_detection_is_listed_first(self):
        csv_text = (
            HEADER
            + b'39.0,33.0,310.0,2026-11-02,0100,n,4.0,N\n'
            + b'38.0,32.0,320.0,2026-11-02,1030,h,9.0,D\n'
        )
        with tempfile.TemporaryDirectory() as folder:
            recent = update_readme.load_last_24_hours(self.NOW, self.write_archive(folder, csv_text))

        table = update_readme.build_table(recent)

        self.assertLess(table.index('10:30'), table.index('01:00'))
        self.assertIn('Yüksek', table)


if __name__ == '__main__':
    unittest.main()
