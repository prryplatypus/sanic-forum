from dataclasses import dataclass
from uuid import UUID

from sanic.exceptions import BadRequest


@dataclass
class CreateCategoryRequest:
    parent_category_id: str
    name: str
    display_order: int

    def __post_init__(self):
        name_len = len(self.name)

        if name_len < 5 or name_len > 250:
            raise BadRequest("Name must be between 5 and 250 characters")

        if self.display_order < 0:
            raise BadRequest("Display order must be a positive integer")

        try:
            UUID(self.parent_category_id)
        except ValueError:
            raise BadRequest("Parent category id must be a UUID")
