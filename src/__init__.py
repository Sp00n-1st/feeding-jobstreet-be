from flask import Flask

app = Flask(__name__)

from src import controller

app.register_blueprint(controller.health_route, url_prefix='/api/v1')
