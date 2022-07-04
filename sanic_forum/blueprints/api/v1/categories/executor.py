from typing import List
from uuid import UUID

from mayim import PostgresExecutor, register

from sanic_forum.database.models import Category


@register
class CategoryExecutor(PostgresExecutor):
    async def insert_category(
        self, parent_category_id: UUID, name: str, display_order: int
    ) -> Category:
        ...

    async def select_all_categories(self) -> List[Category]:
        ...

    async def select_category_by_name(
        self, parent_category_id: UUID, name: str
    ) -> Category:
        ...

    async def update_categories_display_order_for_insert(
        self, parent_category_id: UUID, display_order: int
    ) -> None:
        ...
