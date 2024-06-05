import flask
from flask import request
import os
from bot import ImageProcessingBot

app = flask.Flask(__name__)

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
TELEGRAM_APP_URL = os.environ.get('TELEGRAM_APP_URL')

if not TELEGRAM_TOKEN or not TELEGRAM_APP_URL:
    raise ValueError("TELEGRAM_TOKEN and TELEGRAM_APP_URL must be set in environment variables")

bot = ImageProcessingBot(TELEGRAM_TOKEN, TELEGRAM_APP_URL)


@app.route('/', methods=['GET'])
def index():
    return 'Ok'


@app.route(f'/{TELEGRAM_TOKEN}/', methods=['POST'])
def webhook():
    req = request.get_json()
    try:
        bot.handle_message(req['message'])
    except Exception as e:
        print(f"Error handling message: {e}")
    return 'Ok'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8443)
