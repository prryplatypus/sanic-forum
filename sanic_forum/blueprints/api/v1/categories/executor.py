from typing import List
from uuid import UUID

from mayim import PostgresExecutor, register

from sanic_forum.database.models import Category


@register
class CategoryExecutor(PostgresExecutor):
    async def create_and_return(
        self, parent_category_id: UUID, name: str, display_order: int
    ) -> Category:
        ...

    async def select_all(self) -> List[Category]:
        ...

    async def select_bool_by_name(
        self, parent_category_id: UUID, name: str
    ) -> bool:
        ...

    async def update_for_insert(
        self, parent_category_id: UUID, display_order: int
    ) -> None:
        ...
