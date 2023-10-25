import json
from flask import Blueprint, jsonify, request
from app.controller.bot_controller import BotController

blueprint = Blueprint('bot', __name__)
controller = BotController()


@blueprint.route('/send_message', methods=['POST'])
def send_message(chat_id):
    data = request.data
    decoded_data = data.decode('utf-8')
    json_object = json.loads(decoded_data)
    text = json_object['text']
    parse_mode = json_object.get('parse_mode', 'HTML')

    result = controller.send_message(chat_id, text, parse_mode)
    return jsonify({"message_id": result.message_id}), 200


@blueprint.route('/edit_message_text/<message_id>', methods=['POST'])
def edit_message_text(chat_id, message_id):
    data = request.data
    decoded_data = data.decode('utf-8')
    json_object = json.loads(decoded_data)
    text = json_object['text']
    parse_mode = json_object.get('parse_mode', 'HTML')

    result = controller.edit_message_text(
        chat_id, text, message_id, parse_mode)
    return jsonify({"message_id": result.message_id}), 200


@blueprint.route('/delete_message/<message_id>', methods=['DELETE'])
def delete_message(chat_id, message_id):
    result = controller.delete_message(chat_id, message_id)
    return jsonify("successful"), 200


@blueprint.route('/pin_chat_message/<message_id>', methods=['POST'])
def pin_chat_message(chat_id, message_id):
    data = request.data
    decoded_data = data.decode('utf-8')
    json_object = json.loads(decoded_data)
    disable_notification = json_object.get('disable_notification', False)

    result = controller.pin_chat_message(
        chat_id, message_id, disable_notification)
    return jsonify("successful"), 200
