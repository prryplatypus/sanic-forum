import pytest

from sanic_testing import TestManager

from sanic_forum.app import App, create


@pytest.fixture(scope="session")
def bp_testing_app() -> App:
    app_ = create([
        "sanic_forum.blueprints",
        "sanic_forum.extensions",
        "sanic_forum.pagination",
    ])
    TestManager(app_)
    return app_
