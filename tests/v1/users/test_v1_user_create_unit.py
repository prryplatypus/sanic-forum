from unittest.mock import patch
from mayim.exception import RecordNotFound

from sanic_forum.blueprints.api.v1.users.executor import UserExecutor


def request_body(user):
    return {
        "username": user.username
    }


def test_executor_is_not_used_with_invalid_request(bp_testing_app, mayim):
    with patch(
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        data = {"invalid_field": "abcdefg"}
        bp_testing_app.test_client.post(
            "/api/v1/users", json=data
        )
    mayim.get.assert_not_called()


def test_correct_executor_is_requested(bp_testing_app, mayim, user):
    with patch(
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        bp_testing_app.test_client.post(
            "/api/v1/users", json=request_body(user)
        )
    mayim.get.assert_called_once_with(UserExecutor)


def test_executor_is_used_to_check_for_existing_username(
    bp_testing_app, mayim, user, user_executor
):
    with patch(
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        bp_testing_app.test_client.post(
            "/api/v1/users", json=request_body(user)
        )

    user_executor.select_user_by_username.assert_called_once_with(
        user.username
    )


def test_user_is_not_inserted_if_username_exists(
    bp_testing_app, mayim, user, user_executor
):
    with patch(
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        bp_testing_app.test_client.post(
            "/api/v1/users", json=request_body(user)
        )

    user_executor.insert_user.assert_not_called()


def test_username_is_inserted_if_username_is_valid(
    bp_testing_app, mayim, user, user_executor
):
    user_executor.select_user_by_username.side_effect = RecordNotFound

    with patch(
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        bp_testing_app.test_client.post(
            "/api/v1/users", json=request_body(user)
        )

    user_executor.insert_user.assert_called_once_with(user.username)
