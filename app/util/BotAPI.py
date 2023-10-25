import os
import traceback
from pytgbot import Bot
from app.config.config import Config
import logging
logging.basicConfig(level=logging.DEBUG)


class BotAPI:
    def __init__(self, chat_id):
        self.bot = Bot(Config.bot_api_key)
        self.chat = chat_id

    def send_message(self, text, parse_mode="HTML"):
        result = self.bot.send_message(self.chat, text, parse_mode)
        return result

    def announce(self, error, extra_message=None):
        traceback_str = traceback.format_exc()
        error_message = str(error)
        if extra_message:
            error_message = extra_message + " " + error_message
        message = f"{error_message}\n\n{traceback_str}"
        print(message)
        self.send(message)

    def edit_message_text(self, text, message_id, parse_mode="HTML"):
        result = self.bot.edit_message_text(
            text=text, chat_id=self.chat, message_id=message_id, parse_mode=parse_mode)
        return result

    def delete_message(self, message_id):
        result = self.bot.delete_message(self.chat, message_id)
        return result

    def pin_chat_message(self, message_id, disable_notification):
        result = self.bot.pin_chat_message(
            self.chat, message_id, disable_notification)
        return result
