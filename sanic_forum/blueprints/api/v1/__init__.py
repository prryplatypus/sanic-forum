from sanic import Blueprint

from . import user

bp = Blueprint.group(user.bp, version=1)
