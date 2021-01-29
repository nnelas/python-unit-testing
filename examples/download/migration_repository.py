import random


class MigrationRepository:
    def __init__(self):
        pass

    def exists(self, md5sum: str) -> bool:
        return bool(random.getrandbits(1))
