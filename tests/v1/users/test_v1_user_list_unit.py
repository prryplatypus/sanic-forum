from unittest.mock import patch

from sanic_forum.blueprints.api.v1.users.executor import UserExecutor


def test_correct_executor_is_requested(bp_testing_app, mayim):
    with patch(
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        bp_testing_app.test_client.get("/api/v1/users")
    mayim.get.assert_called_once_with(UserExecutor)


def test_executor_is_called_with_expected_parameters(
    bp_testing_app, mayim, user_executor
):
    with patch(
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        bp_testing_app.test_client.get("/api/v1/users?limit=1&offset=5")
    user_executor.select_all_users.assert_called_once_with(1, 5)
