from mayim import Mayim
from sanic import Blueprint
from sanic.exceptions import BadRequest
from sanic.request import Request
from sanic.response import HTTPResponse, json
from sanic_ext import validate

from .executor import CategoryExecutor
from .requests import CreateCategoryRequest

bp = Blueprint("api-v1-categories", url_prefix="/categories")


@bp.get("")
async def list_all_categories(_: Request) -> HTTPResponse:
    executor = Mayim.get(CategoryExecutor)
    categories = await executor.select_all()
    return json([category.to_dict() for category in categories])


@bp.post("")
@validate(json=CreateCategoryRequest)
async def create_category(
    _: Request, body: CreateCategoryRequest
) -> HTTPResponse:
    executor = Mayim.get(CategoryExecutor)

    qargs = (body.parent_category_id,)
    if not (await executor.select_bool_by_id(*qargs)):
        raise BadRequest("Unknown parent category")

    qargs = (body.parent_category_id, body.name)
    if await executor.select_bool_by_name(*qargs):
        raise BadRequest("Name is already in use")

    qargs = (body.parent_category_id, body.display_order)
    await executor.update_for_insert(*qargs)

    qargs = (body.parent_category_id, body.name, body.display_order)
    category = await executor.insert_and_return(*qargs)

    return json(category.to_dict())
