from mayim import Mayim
from mayim.exception import RecordNotFound
from sanic import Blueprint
from sanic.exceptions import InvalidUsage
from sanic.request import Request
from sanic.response import HTTPResponse, json
from sanic_ext import validate

from .executor import UserExecutor
from .requests import CreateUserRequest
from sanic_forum.pagination import Pagination

bp = Blueprint("api-v1-users", url_prefix="/users")


@bp.get("")
async def list_all_users(_: Request, pagination: Pagination) -> HTTPResponse:
    executor = Mayim.get(UserExecutor)
    users = await executor.select_all_users(
        pagination.limit, pagination.offset
    )
    return json([user.to_dict() for user in users])


@bp.post("")
@validate(json=CreateUserRequest)
async def create_user(_: Request, body: CreateUserRequest) -> HTTPResponse:
    executor = Mayim.get(UserExecutor)

    try:
        await executor.select_user_by_username(body.username)
    except RecordNotFound:
        pass
    else:
        raise InvalidUsage("Username is not available")

    user = await executor.insert_user(body.username)

    return json(user.to_dict())
