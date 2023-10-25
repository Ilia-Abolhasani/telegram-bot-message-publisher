from app.route.bot_route import blueprint as bot_route
from flask import Blueprint, jsonify

route_bp = Blueprint('route', __name__)

route_bp.register_blueprint(bot_route, url_prefix='/api/bot/<int:chat_id>')


@route_bp.route('/api/test', methods=['GET'])
def test_route():
    return jsonify(message="successful"), 200
