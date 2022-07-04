from sanic import Blueprint

from . import categories, users

bp = Blueprint.group(categories.bp, users.bp, version=1)
