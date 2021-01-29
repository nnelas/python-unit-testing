import re
from typing import Optional

from examples.auth.http_request import HTTPRequest
from examples.auth.jwt_requests_validator import JwtRequestsValidator


class AuthenticationManager:
    def __init__(self, jwt_requests_validator: JwtRequestsValidator):
        self.__jwt_requests_validator = jwt_requests_validator

    def validate(self, request: HTTPRequest) -> bool:
        if request.path == "/status":
            return True

        if request.headers.get("team") == "internal":
            jwt_token = self.__get_jwt_token(request.headers)
            if jwt_token is None:
                return False
            return self.__jwt_requests_validator.validate(jwt_token)
        return True

    def __get_jwt_token(self, headers: dict) -> Optional[str]:
        token = headers.get("Authorization")
        if token is None:
            return None
        match = re.search(r"Bearer\s(.+)", token)
        return match.group(1) if match else None
