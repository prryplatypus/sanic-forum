from typing import List

from mayim import PostgresExecutor, register

from .model import User


@register
class UserExecutor(PostgresExecutor):
    async def select_all_users(self) -> List[User]:
        ...
