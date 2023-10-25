from app.util.BotAPI import BotAPI


class BotController:
    def _bot(channel_id):
        return BotAPI(channel_id)

    def send_message(self, chat_id, text, parse_mode="HTML"):
        return self._bot(chat_id).send_message(text, parse_mode)

    def edit_message_text(self, chat_id, text, message_id, parse_mode="HTML"):
        return self._bot(chat_id).edit_message_text(text,  message_id, parse_mode)

    def delete_message(self, chat_id, message_id):
        return self._bot(chat_id).delete_message(message_id)

    def pin_chat_message(self, chat_id, message_id, disable_notification):
        return self._bot(chat_id).pin_chat_message(message_id, disable_notification)
