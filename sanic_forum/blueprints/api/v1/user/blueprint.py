from mayim import Mayim
from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, json

from .executor import UserExecutor
from sanic_forum.pagination import Pagination

bp = Blueprint("api-v1-users", url_prefix="/users")


@bp.get("")
async def ping_human(_: Request, pagination: Pagination) -> HTTPResponse:
    executor = Mayim.get(UserExecutor)
    users = await executor.select_all_users(
        pagination.limit, pagination.offset
    )
    return json([user.as_dict() for user in users])
