from sanic_ext.extensions.injection.extension import InjectionExtension
# from sanic_ext.extensions.openapi.extension import OpenAPIExtension

from sanic_forum.app import App


def setup(app: App) -> None:
    app.extend(
        extensions=[
            InjectionExtension,
            # OpenAPIExtension,
        ],
        built_in_extensions=False,
    )
