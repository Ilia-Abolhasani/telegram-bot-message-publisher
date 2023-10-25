import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    server_port = os.getenv("server_port")
    bot_api_key = os.getenv("bot_api_key")
    bot_chat_id = os.getenv("bot_chat_id")
