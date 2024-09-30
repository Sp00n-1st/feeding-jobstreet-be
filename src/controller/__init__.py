from flask import Blueprint

health_route = Blueprint('health', __name__)

from . import health
