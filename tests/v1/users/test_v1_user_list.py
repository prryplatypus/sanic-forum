from unittest.mock import patch


def test_users_can_be_listed(bp_testing_app, mayim, user):
    with patch(
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        _, resp = bp_testing_app.test_client.get("/api/v1/users")
    assert resp.json == [user.to_dict()]


def test_executor_is_called_with_expected_parameters(
    bp_testing_app, mayim, user_executor
):
    with patch(
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        bp_testing_app.test_client.get("/api/v1/users?limit=1&offset=5")
    user_executor.select_all_users.assert_called_once_with(1, 5)
