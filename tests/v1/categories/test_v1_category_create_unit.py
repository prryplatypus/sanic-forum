import pytest
from unittest.mock import patch

from sanic_forum.blueprints.api.v1.categories.executor import CategoryExecutor


def test_correct_executor_is_used(bp_testing_app, mayim, root_category):
    with patch(
        "sanic_forum.blueprints.api.v1.categories.blueprint.Mayim", mayim
    ):
        data = {
            "parent_category_id": str(root_category.id),
            "name": "Test Category",
            "display_order": 0,
        }

        bp_testing_app.test_client.post(
            "/api/v1/categories", json=data
        )

    mayim.get.assert_called_once_with(CategoryExecutor)


def test_executor_is_not_used_if_validation_fails(bp_testing_app, mayim):
    with patch(
        "sanic_forum.blueprints.api.v1.categories.blueprint.Mayim", mayim
    ):
        data = {"invalid": "data"}
        bp_testing_app.test_client.post("/api/v1/categories", json=data)

    mayim.get.assert_not_called()


def test_parent_existence_is_checked_by_id(
    bp_testing_app, category_executor, mayim, root_category
):
    parent_category_id = str(root_category.id)

    with patch(
        "sanic_forum.blueprints.api.v1.categories.blueprint.Mayim", mayim
    ):
        data = {
            "parent_category_id": parent_category_id,
            "name": "Test Category",
            "display_order": 0,
        }
        bp_testing_app.test_client.post("/api/v1/categories", json=data)

    category_executor.select_bool_by_id.assert_called_once_with(
        parent_category_id
    )


def test_name_existence_is_checked_by_parent_id_and_name(
    bp_testing_app, category_executor, mayim, root_category
):
    parent_category_id = str(root_category.id)
    name = "Test Category"

    with patch(
        "sanic_forum.blueprints.api.v1.categories.blueprint.Mayim", mayim
    ):
        data = {
            "parent_category_id": parent_category_id,
            "name": name,
            "display_order": 0,
        }
        bp_testing_app.test_client.post("/api/v1/categories", json=data)

    category_executor.select_bool_by_name.assert_called_once_with(
        parent_category_id, name
    )


@pytest.mark.parametrize(
    "method,retval",
    [
        ("select_bool_by_id", False),
        ("select_bool_by_name", True),
    ]
)
def test_categories_are_not_affected_if_checks_fail(
    bp_testing_app, category_executor, mayim, root_category, method, retval
):
    getattr(category_executor, method).return_value = retval

    with patch(
        "sanic_forum.blueprints.api.v1.categories.blueprint.Mayim", mayim
    ):
        data = {
            "parent_category_id": str(root_category.id),
            "name": "Test category",
            "display_order": 0,
        }
        bp_testing_app.test_client.post("/api/v1/categories", json=data)

    category_executor.update_for_insert.assert_not_called()
    category_executor.insert_and_return.assert_not_called()


def test_category_positions_are_updated_with_parent_category_and_display_order(
    bp_testing_app, category_executor, mayim, root_category
):
    parent_category_id = str(root_category.id)
    display_order = 0

    with patch(
        "sanic_forum.blueprints.api.v1.categories.blueprint.Mayim", mayim
    ):
        data = {
            "parent_category_id": parent_category_id,
            "name": "Test category",
            "display_order": display_order,
        }
        bp_testing_app.test_client.post("/api/v1/categories", json=data)

    category_executor.update_for_insert.assert_called_once_with(
        parent_category_id, display_order
    )


def test_category_positions_are_updated_before_insert(
    bp_testing_app, category_executor, mayim, root_category
):
    # We want it to raise an Exception so execution stops there.
    category_executor.update_for_insert.side_effect = Exception

    with patch(
        "sanic_forum.blueprints.api.v1.categories.blueprint.Mayim", mayim
    ):
        data = {
            "parent_category_id": str(root_category.id),
            "name": "Test category",
            "display_order": 0,
        }
        bp_testing_app.test_client.post("/api/v1/categories", json=data)

    category_executor.update_for_insert.assert_called_once()
    category_executor.insert_and_return.assert_not_called()


def test_category_is_inserted_with_expected_parameters(
    bp_testing_app, category_executor, mayim, root_category
):
    parent_category_id = str(root_category.id)
    name = "Test category"
    display_order = 0

    with patch(
        "sanic_forum.blueprints.api.v1.categories.blueprint.Mayim", mayim
    ):
        data = {
            "parent_category_id": parent_category_id,
            "name": name,
            "display_order": display_order,
        }
        bp_testing_app.test_client.post("/api/v1/categories", json=data)

    category_executor.insert_and_return.assert_called_once_with(
        parent_category_id, name, display_order
    )
