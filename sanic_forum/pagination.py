from __future__ import annotations

from dataclasses import dataclass, field

from sanic import Request

from sanic_forum.app import App


@dataclass
class Pagination(object):
    limit: int = field(default=15)
    offset: int = field(default=0)

    @staticmethod
    async def from_request(request: Request) -> Pagination:
        args = {
            key: int(value)
            for key in ("limit", "offset")
            if (value := request.args.get(key))
        }
        return Pagination(**args)


def setup(app: App) -> None:
    app.ext.add_dependency(Pagination, Pagination.from_request)
