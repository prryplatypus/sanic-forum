from unittest.mock import patch


def test_unknown_parameters_raise_bad_request_error(bp_testing_app, mayim):
    with patch(
        "sanic_forum.blueprints.api.v1.categories.blueprint.Mayim", mayim
    ):
        data = {"invalid_field": "abcdefg"}
        _, resp = bp_testing_app.test_client.post(
            "/api/v1/categories", json=data
        )

    assert resp.status == 400


def test_known_parameters_are_accepted(bp_testing_app, mayim, root_category):
    with patch(
        "sanic_forum.blueprints.api.v1.categories.blueprint.Mayim", mayim
    ):
        data = {
            "parent_category_id": str(root_category.id),
            "name": "Test Category",
            "display_order": 0,
        }

        _, resp = bp_testing_app.test_client.post(
            "/api/v1/categories", json=data
        )

    assert resp.status == 200


def test_unknown_parent_category_raises_bad_request(
    bp_testing_app, category_executor, mayim, root_category
):
    category_executor.select_bool_by_id.return_value = False

    with patch(
        "sanic_forum.blueprints.api.v1.categories.blueprint.Mayim", mayim
    ):
        data = {
            "parent_category_id": str(root_category.id),
            "name": "Test Category",
            "display_order": 0,
        }

        _, resp = bp_testing_app.test_client.post(
            "/api/v1/categories", json=data
        )

    assert resp.status == 400


def test_duplicate_category_name_raises_bad_request(
    bp_testing_app, category_executor, mayim, root_category
):
    category_executor.select_bool_by_name.return_value = True

    with patch(
        "sanic_forum.blueprints.api.v1.categories.blueprint.Mayim", mayim
    ):
        data = {
            "parent_category_id": str(root_category.id),
            "name": "Test Category",
            "display_order": 0,
        }

        _, resp = bp_testing_app.test_client.post(
            "/api/v1/categories", json=data
        )

    assert resp.status == 400


def test_created_category_is_returned(
    bp_testing_app, category, mayim, root_category
):
    with patch(
        "sanic_forum.blueprints.api.v1.categories.blueprint.Mayim", mayim
    ):
        data = {
            "parent_category_id": str(root_category.id),
            "name": category.name,
            "display_order": category.display_order,
        }

        _, resp = bp_testing_app.test_client.post(
            "/api/v1/categories", json=data
        )

    assert resp.status == 200
    assert resp.json == category.to_dict()
