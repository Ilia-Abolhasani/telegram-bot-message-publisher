from app.util.BotAPI import BotAPI


class BotController:
    def _bot(self, chat_id):
        return BotAPI(chat_id)

    def send_message(self, chat_id, text, parse_mode="HTML"):
        bot = self._bot(chat_id)
        return bot.send_message(text, parse_mode)

    def edit_message_text(self, chat_id, text, message_id, parse_mode="HTML"):
        bot = self._bot(chat_id)
        return bot.edit_message_text(text,  message_id, parse_mode)

    def delete_message(self, chat_id, message_id):
        bot = self._bot(chat_id)
        return bot.delete_message(message_id)

    def pin_chat_message(self, chat_id, message_id, disable_notification):
        bot = self._bot(chat_id)
        return bot.pin_chat_message(message_id, disable_notification)
