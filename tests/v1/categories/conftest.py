import pytest
import uuid
from unittest.mock import AsyncMock, Mock

from sanic_forum.database.models import Category


@pytest.fixture
def root_category():
    return Category(
        id=uuid.uuid4(),
        parent_category_id=None,
        name="root",
        display_order=0,
    )


@pytest.fixture
def category(root_category):
    return Category(
        id=uuid.uuid4(),
        parent_category_id=root_category.id,
        name="Main",
        display_order=0,
    )


@pytest.fixture
def category_executor(root_category, category):
    executor = Mock()
    executor.select_all_categories = AsyncMock(
        return_value=[root_category, category]
    )
    return executor


@pytest.fixture
def mayim(category_executor):
    mayim = Mock()
    mayim.get = Mock(return_value=category_executor)
    return mayim
