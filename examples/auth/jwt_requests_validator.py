import random


class JwtRequestsValidator:
    def __init__(self):
        pass

    def validate(self, jwt_token: str) -> bool:
        return bool(random.getrandbits(1))
