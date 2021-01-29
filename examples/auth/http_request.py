class HTTPRequest:
    def __init__(self, path: str, headers: dict):
        self.path = path
        self.headers = headers
