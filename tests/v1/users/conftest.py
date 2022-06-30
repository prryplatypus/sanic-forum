import pytest
import uuid
from unittest.mock import AsyncMock, Mock

from sanic_forum.database.models import User


@pytest.fixture
def user():
    return User(id=uuid.uuid4(), username="test")


@pytest.fixture
def user_executor(user):
    executor = Mock()
    executor.insert_user = AsyncMock(return_value=user)
    executor.select_all_users = AsyncMock(return_value=[user])
    executor.select_user_by_username = AsyncMock(return_value=user)
    return executor


@pytest.fixture
def mayim(user_executor):
    mayim = Mock()
    mayim.get = Mock(return_value=user_executor)
    return mayim
