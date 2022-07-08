from unittest.mock import patch

from sanic_forum.blueprints.api.v1.categories.executor import CategoryExecutor


def test_correct_executor_is_requested(bp_testing_app, mayim):
    with patch(
        "sanic_forum.blueprints.api.v1.categories.blueprint.Mayim", mayim
    ):
        bp_testing_app.test_client.get("/api/v1/categories")
    mayim.get.assert_called_once_with(CategoryExecutor)


def test_expected_executor_method_is_called(
    bp_testing_app, category_executor, mayim
):
    with patch(
        "sanic_forum.blueprints.api.v1.categories.blueprint.Mayim", mayim
    ):
        bp_testing_app.test_client.get("/api/v1/categories")
    category_executor.select_all.assert_called_once_with()
