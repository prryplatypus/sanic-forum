from mayim import Mayim
from mayim.exception import RecordNotFound
from sanic import Blueprint
from sanic.exceptions import InvalidUsage
from sanic.request import Request
from sanic.response import HTTPResponse, json
from sanic_ext import validate

from .executor import CategoryExecutor
from .requests import CreateCategoryRequest

# from sanic_forum.pagination import Pagination

bp = Blueprint("api-v1-categories", url_prefix="/categories")


@bp.get("")
async def list_all_categories(_: Request) -> HTTPResponse:
    executor = Mayim.get(CategoryExecutor)
    categories = await executor.select_all_categories()
    return json([category.to_dict() for category in categories])


@bp.post("")
@validate(json=CreateCategoryRequest)
async def create_category(
    _: Request, body: CreateCategoryRequest
) -> HTTPResponse:
    executor = Mayim.get(CategoryExecutor)

    try:
        await executor.select_category_by_name(
            body.parent_category_id, body.name
        )
    except RecordNotFound:
        pass
    else:
        raise InvalidUsage("Name is already in use")

    category = await executor.insert_category(
        body.parent_category_id, body.name, body.display_order
    )

    return json(category.to_dict())
