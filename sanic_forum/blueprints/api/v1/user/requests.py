from dataclasses import dataclass

from sanic.exceptions import InvalidUsage


@dataclass
class CreateUserRequest:
    username: str

    def __post_init__(self):
        length = len(self.username)

        if length < 5 or length > 20:
            raise InvalidUsage("Username must be between 5 and 20 characters")
