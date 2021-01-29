import os

from examples.download.migration_repository import MigrationRepository


class ApkNotFoundException(Exception):
    pass


class DownloaderService:
    def __init__(self, migration_repository: MigrationRepository):
        self.__migration_repository = migration_repository

    def get_download_path(self, md5sum: str):
        download_path = os.path.join("/tmp", "testing", md5sum)
        if os.path.isfile(download_path):
            return download_path
        elif self.__migration_repository.exists(md5sum):
            raise ApkNotFoundException("Migration with more than 1 month")
        else:
            raise ApkNotFoundException("No APK found for the provided MD5 sum")
