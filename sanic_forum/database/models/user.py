from uuid import UUID

from .__base__ import BaseModel


class User(BaseModel):
    def __init__(self, *, id: UUID, username: str) -> None:
        self.id = id
        self.username = username

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "username": self.username,
        }
