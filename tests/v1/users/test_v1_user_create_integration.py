from unittest.mock import patch
from mayim.exception import RecordNotFound


def test_invalid_requests_are_rejected(bp_testing_app, mayim, user_executor):
    # Ensure existing username check doesn't fail
    user_executor.select_user_by_username.side_effect = RecordNotFound

    with patch(
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        data = {"invalid_field": "abcdefg"}
        _, resp = bp_testing_app.test_client.post("/api/v1/users", json=data)

    assert resp.status == 400


def test_request_fails_if_valid_username_in_use(
    bp_testing_app, mayim, user
):
    with patch(  # The mayim mock always returns a user
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        data = {"username": user.username}
        _, resp = bp_testing_app.test_client.post("/api/v1/users", json=data)

    assert resp.status == 400


def test_request_succeeds_if_valid_username_available(
    bp_testing_app, mayim, user_executor, user
):
    # Ensure existing username check doesn't fail
    user_executor.select_user_by_username.side_effect = RecordNotFound

    with patch(
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        data = {"username": user.username}
        _, resp = bp_testing_app.test_client.post("/api/v1/users", json=data)

    assert resp.status == 200
    assert resp.json == user.to_dict()


def test_request_fails_with_username_len_under_lower_bound(
    bp_testing_app, mayim, user_executor
):
    # Ensure existing username check doesn't fail
    user_executor.select_user_by_username.side_effect = RecordNotFound

    with patch(
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        data = {"username": "abcd"}
        _, resp = bp_testing_app.test_client.post("/api/v1/users", json=data)

    assert resp.status == 400


def test_request_succeeds_with_username_len_lower_bound(
    bp_testing_app, mayim, user_executor
):
    # Ensure existing username check doesn't fail
    user_executor.select_user_by_username.side_effect = RecordNotFound

    with patch(
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        data = {"username": "abcde"}
        _, resp = bp_testing_app.test_client.post("/api/v1/users", json=data)

    assert resp.status == 200


def test_request_succeeds_with_username_len_upper_bound(
    bp_testing_app, mayim, user_executor
):
    # Ensure existing username check doesn't fail
    user_executor.select_user_by_username.side_effect = RecordNotFound

    with patch(
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        data = {"username": ("abcde" * 4)}
        _, resp = bp_testing_app.test_client.post("/api/v1/users", json=data)

    assert resp.status == 200


def test_request_succeeds_with_username_len_over_upper_bound(
    bp_testing_app, mayim, user_executor
):
    # Ensure existing username check doesn't fail
    user_executor.select_user_by_username.side_effect = RecordNotFound

    with patch(
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        data = {"username": ("abcde" * 4) + "f"}
        _, resp = bp_testing_app.test_client.post("/api/v1/users", json=data)

    assert resp.status == 400
