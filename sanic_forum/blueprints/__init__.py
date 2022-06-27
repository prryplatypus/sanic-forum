from . import api
from sanic_forum.app import App


def setup(app: App):
    app.blueprint(api.bp)
