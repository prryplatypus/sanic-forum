from typing import Optional
from uuid import UUID

from .__base__ import BaseModel


class Category(BaseModel):
    def __init__(
        self,
        *,
        id: UUID,
        parent_category_id: Optional[UUID],
        name: str,
        display_order: int
    ) -> None:
        self.id = id
        self.parent_category_id = parent_category_id
        self.name = name
        self.display_order = display_order

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "parent_category_id": (
                str(self.parent_category_id)
                if self.parent_category_id
                else None
            ),
            "name": self.name,
            "display_order": self.display_order,
        }
