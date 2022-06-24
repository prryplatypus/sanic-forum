from __future__ import annotations

from mayim import Mayim

from sanic_forum.app import App
from sanic_forum.constants import APP_NAME


app = App.get_app(APP_NAME)


@app.before_server_start
async def connect_database(*_):
    app.ctx.mayim = Mayim(dsn=app.config.DATABASE_URL)


# @app.after_server_stop
# async def disconnect_database(*_):
#     await pool.disconnect()
