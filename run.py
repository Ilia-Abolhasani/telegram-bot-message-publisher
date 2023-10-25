from app import app
from app.middleware import error_handler
from app.config.config import Config

if __name__ == '__main__':
    error_handler.register_error_handlers(app)
    app.run(debug=False, host="0.0.0.0", port=Config.server_port)
