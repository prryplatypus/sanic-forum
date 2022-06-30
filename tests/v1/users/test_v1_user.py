import uuid

from sanic_forum.database.models import User


def test_user_has_expected_properties():
    id = uuid.uuid4()
    user = User(id=id, username="test")
    assert user.id == id
    assert user.username == "test"


def test_user_to_dict_method(user):
    assert user.to_dict() == {
        "id": str(user.id),
        "username": user.username,
    }
