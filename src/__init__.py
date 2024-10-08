from flask import Flask
from flask_cors import CORS
from src.config import config

app = Flask(__name__)

CORS(app, origins=["http://localhost:5050"])

from src import controller
app.register_blueprint(controller.health_route, url_prefix='/api/v1')

app.register_blueprint(controller.job_route, url_prefix=config.URL_PREFIX)
