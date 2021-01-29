import os
import unittest
from unittest import mock

from examples.auth.authentication_manager import AuthenticationManager
from examples.auth.http_request import HTTPRequest
from examples.auth.jwt_requests_validator import JwtRequestsValidator
from examples.download.downloader_service import DownloaderService, ApkNotFoundException
from examples.download.migration_repository import MigrationRepository


class TestAuthenticationManager(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.authentication_manager: AuthenticationManager = None

    def setUp(self) -> None:
        self.authentication_manager = AuthenticationManager(JwtRequestsValidator())

    def test_validate_on_path_status(self):
        request = HTTPRequest("/status", {})
        valid = self.authentication_manager.validate(request)
        self.assertEqual(valid, True)

    def test_validate_on_team_not_internal(self):
        request = HTTPRequest("/migration/list", {"team": "appcoins"})
        valid = self.authentication_manager.validate(request)
        self.assertEqual(valid, True)

    def test_validate_on_team_internal_without_jwt(self):
        request = HTTPRequest(
            "/migration/list",
            {"team": "internal", "Authorization": "Basic A_RANDOM_TOKEN"},
        )
        valid = self.authentication_manager.validate(request)
        self.assertEqual(valid, False)

    @mock.patch.object(JwtRequestsValidator, "validate")
    def test_validate_on_team_internal_with_jwt(self, mock_validate):
        mock_validate.return_value = True
        request = HTTPRequest(
            "/migration/list",
            {"team": "internal", "Authorization": "Bearer A_RANDOM_TOKEN"},
        )
        valid = self.authentication_manager.validate(request)
        self.assertEqual(valid, True)
