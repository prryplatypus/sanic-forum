from typing import List

from mayim import PostgresExecutor, register

from sanic_forum.database.models import User


@register
class UserExecutor(PostgresExecutor):
    async def select_all_users(self) -> List[User]:
        ...
