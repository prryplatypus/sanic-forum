import uuid
import pytest

from sanic_forum.database.models import Category


@pytest.mark.parametrize(
    "id,parent_category_id,name,display_order",
    [
        (uuid.uuid4(), None, "root", 0),
        (uuid.uuid4(), uuid.uuid4(), "Main", 0),
    ]
)
def test_category_properties(
    id, parent_category_id, name, display_order
):
    category = Category(
        id=id,
        parent_category_id=parent_category_id,
        name=name,
        display_order=display_order,
    )
    assert category.id == id
    assert category.parent_category_id == parent_category_id
    assert category.name == name
    assert category.display_order == display_order


def test_category_to_dict_method(category):
    assert category.to_dict() == {
        "id": str(category.id),
        "parent_category_id": (
            str(category.parent_category_id)
            if category.parent_category_id else None
        ),
        "name": category.name,
        "display_order": category.display_order,
    }
