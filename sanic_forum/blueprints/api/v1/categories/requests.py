from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from sanic.exceptions import InvalidUsage


@dataclass
class CreateCategoryRequest:
    parent_category_id: Optional[UUID]
    name: str
    display_order: int

    def __post_init__(self):
        name_len = len(self.name)

        if name_len < 5 or name_len > 250:
            raise InvalidUsage("Name must be between 5 and 250 characters")

        if self.display_order < 0:
            raise InvalidUsage("Display order must be a positive integer")
