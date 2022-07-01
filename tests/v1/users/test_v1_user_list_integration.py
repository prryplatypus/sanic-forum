from unittest.mock import patch


def test_users_can_be_listed(bp_testing_app, mayim, user):
    with patch(
        "sanic_forum.blueprints.api.v1.users.blueprint.Mayim", mayim
    ):
        _, resp = bp_testing_app.test_client.get("/api/v1/users")
    assert resp.json == [user.to_dict()]
