from typing import List

from mayim import PostgresExecutor, register

from sanic_forum.database.models import User


@register
class UserExecutor(PostgresExecutor):
    async def insert_user(self, username: str) -> User:
        ...

    async def select_all_users(self, limit: int, offset: int) -> List[User]:
        ...

    async def select_user_by_username(self, username: str) -> User:
        ...
