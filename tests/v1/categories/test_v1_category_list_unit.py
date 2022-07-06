from unittest.mock import patch

from sanic_forum.blueprints.api.v1.categories.executor import CategoryExecutor


def test_correct_executor_is_requested(bp_testing_app, mayim):
    with patch(
        "sanic_forum.blueprints.api.v1.categories.blueprint.Mayim", mayim
    ):
        bp_testing_app.test_client.get("/api/v1/categories")
    mayim.get.assert_called_once_with(CategoryExecutor)
