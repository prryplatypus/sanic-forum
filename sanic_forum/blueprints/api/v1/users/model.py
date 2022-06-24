from uuid import UUID


class User(object):
    def __init__(self, *, id: UUID, username: str) -> None:
        self.id = id
        self.username = username

    def as_dict(self) -> dict:
        return {
            "id": str(self.id),
            "username": self.username,
        }
