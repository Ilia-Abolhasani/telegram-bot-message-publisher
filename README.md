# Telegram Bot Message Publisher

This repository hosts a simple web service designed for sending messages via a Telegram bot when direct access to Telegram API and servers is restricted or banned. Messages are received through a POST request to the endpoint `/ {chat_id} /bot/send_message` and are then forwarded to a specified chat ID using the configured Telegram bot.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Ilia-Abolhasani/telegram-bot-message-publisher.git
```
### 2. Navigate to the Project Directory
```bash
cd telegram-bot-message-publisher
```
### 3. Create a .env File
Create a .env file in the root directory and add the following configurations:
```env
Copy code
## server
server_port = 4001

## bot_api_key
bot_api_key = "YOUR_TELEGRAM_BOT_API_KEY"
```
Replace "YOUR_TELEGRAM_BOT_API_KEY" with the actual API key of your Telegram bot.


## Usage

1. **Install Dependencies:**

   Ensure you have Python installed on your system. If not, you can download it [here](https://www.python.org/downloads/).

   Install the required dependencies listed in the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   
2. **Start the Server:**
```bash
python3 app.py
```
The server will run on the specified port (default is 4001).
