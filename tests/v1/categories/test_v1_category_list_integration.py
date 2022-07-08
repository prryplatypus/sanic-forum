from unittest.mock import patch


def test_users_can_be_listed(bp_testing_app, mayim, category_executor):
    with patch(
        "sanic_forum.blueprints.api.v1.categories.blueprint.Mayim", mayim
    ):
        _, resp = bp_testing_app.test_client.get("/api/v1/categories")

    category_dicts = [
        user.to_dict()
        for user in category_executor.select_all.return_value
    ]

    assert resp.json == category_dicts
