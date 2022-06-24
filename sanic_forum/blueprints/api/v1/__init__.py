from sanic import Blueprint

from . import users

bp = Blueprint.group(users.bp, version=1)
