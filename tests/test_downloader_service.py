import os
import unittest
from unittest import mock

from examples.download.downloader_service import DownloaderService, ApkNotFoundException
from examples.download.migration_repository import MigrationRepository


class TestDownloaderService(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.downloader_service: DownloaderService = None

    def setUp(self) -> None:
        self.downloader_service = DownloaderService(MigrationRepository())

    @mock.patch.object(os.path, "isfile")
    def test_get_download_path_when_apk_exists(self, mock_isfile):
        mock_isfile.return_value = True
        path = self.downloader_service.get_download_path("01234")
        expected_path = os.path.join("/tmp", "testing", "01234")
        self.assertEqual(path, expected_path)

    @mock.patch.object(MigrationRepository, "exists")
    def test_get_download_path_when_apk_one_month_old(self, mock_exists):
        mock_exists.return_value = True
        with self.assertRaises(ApkNotFoundException) as e:
            self.downloader_service.get_download_path("01234")
        self.assertEqual(str(e.exception), "Migration with more than 1 month")

    @mock.patch.object(MigrationRepository, "exists")
    def test_get_download_path_when_apk_not_found(self, mock_exists):
        mock_exists.return_value = False
        with self.assertRaises(ApkNotFoundException) as e:
            self.downloader_service.get_download_path("01234")
        self.assertEqual(str(e.exception), "No APK found for the provided MD5 sum")
