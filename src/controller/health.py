from src.controller import health_route
from src.config import config

@health_route.route('/', methods=["GET"])
def home():
    return f"Home of Application {config.APP_NAME}"

@health_route.route('/ping', methods=["GET"])
def ping():
    return f"OK!"
