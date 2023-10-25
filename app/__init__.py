
from flask import Flask
from app.route import route_bp
from app.middleware.request_handler import request_handler_middleware

app = Flask(__name__)
app.register_blueprint(route_bp)
app.before_request(request_handler_middleware)
