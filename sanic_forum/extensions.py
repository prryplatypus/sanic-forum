from sanic_ext import Extend
from sanic_ext.extensions.injection.extension import InjectionExtension
from sanic_ext.extensions.openapi.extension import OpenAPIExtension

from sanic_forum.app import App
from sanic_forum.constants import APP_NAME

app = App.get_app(APP_NAME)

app.extend(
    extensions=[
        InjectionExtension,
        OpenAPIExtension,
    ],
    built_in_extensions=False,
)

assert isinstance(app.ext, Extend)
