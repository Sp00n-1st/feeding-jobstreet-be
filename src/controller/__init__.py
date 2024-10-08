from flask import Blueprint

health_route = Blueprint('health', __name__)

job_route = Blueprint('job', __name__)

from . import health

from . import job_controller
