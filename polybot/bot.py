import telebot
from loguru import logger
import os
import time
from telebot.types import InputFile
from img_proc import Img  # Adjust the import path as necessary


def is_current_msg_photo(msg):
    return 'photo' in msg


class Bot:
    def __init__(self, token, telegram_chat_url):
        self.telegram_bot_client = telebot.TeleBot(token)
        self.telegram_bot_client.remove_webhook()
        time.sleep(0.5)
        self.telegram_bot_client.set_webhook(url=f'{telegram_chat_url}/{token}/', timeout=60)
        logger.info(f'Telegram Bot information\n\n{self.telegram_bot_client.get_me()}')

    def send_text(self, chat_id, text):
        self.telegram_bot_client.send_message(chat_id, text)

    def send_text_with_quote(self, chat_id, text, quoted_msg_id):
        self.telegram_bot_client.send_message(chat_id, text, reply_to_message_id=quoted_msg_id)

    def download_user_photo(self, msg):
        if not is_current_msg_photo(msg):
            raise RuntimeError(f'Message content of type \'photo\' expected')

        file_info = self.telegram_bot_client.get_file(msg['photo'][-1]['file_id'])
        data = self.telegram_bot_client.download_file(file_info.file_path)
        folder_name = Img.BASE_DIR / file_info.file_path.split('/')[0]

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        file_path = folder_name / file_info.file_path.split('/')[-1]
        with open(file_path, 'wb') as photo:
            photo.write(data)

        return file_path

    def send_photo(self, chat_id, img_path):
        if not os.path.exists(img_path):
            raise RuntimeError("Image path doesn't exist")

        self.telegram_bot_client.send_photo(
            chat_id,
            InputFile(img_path)
        )

    def handle_message(self, msg):
        logger.info(f'Incoming message: {msg}')
        self.send_text(msg['chat']['id'], f'Your original message: {msg.get("text", "No text provided.")}')


class QuoteBot(Bot):
    def handle_message(self, msg):
        logger.info(f'Incoming message: {msg}')

        if msg["text"] != 'Please don\'t quote me':
            self.send_text_with_quote(msg['chat']['id'], msg["text"], quoted_msg_id=msg["message_id"])


class ImageProcessingBot(Bot):
    def handle_message(self, msg):
        logger.info(f'Incoming message: {msg}')

        chat_id = msg['chat']['id']

        # Check if the message contains a photo
        if not is_current_msg_photo(msg):
            self.send_text(chat_id,
                           "Please send a photo with a caption specifying the desired action (e.g., blur, rotate, "
                           "etc.).")
            return

        # Download the user's photo
        img_path = self.download_user_photo(msg)
        img = Img(img_path)

        # Process the image based on the caption
        action = msg.get('caption', '').lower()

        if action == 'blur':
            img.blur()
        elif action == 'rotate':
            img.rotate()
        elif action == 'contour':
            img.contour()  # Call the contour function as expected
        elif action == 'salt and pepper':
            img.salt_n_pepper()
        else:
            self.send_text(chat_id,
                           "Unknown action. Please specify one of the following actions in the caption: blur, rotate, "
                           "contour, salt and pepper.")
            return

        # Save the processed image
        processed_img_path = img.save_img(suffix=action.capitalize())

        # Send the processed image back to the user
        self.send_photo(chat_id, processed_img_path)
