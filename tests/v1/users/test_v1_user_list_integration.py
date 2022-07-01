from unittest.mock import patch


def test_users_can_be_listed(bp_testing_app, mayim, user_executor):
    with patch(
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        _, resp = bp_testing_app.test_client.get("/api/v1/users")

    user_dicts = [
        user.to_dict() for user in user_executor.select_all_users.return_value
    ]
    assert resp.json == user_dicts
