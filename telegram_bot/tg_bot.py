import telegram
import os
import random
import logging


logger = logging.getLogger('tg_bot')


def send_photo_to_chat(tg_token, chat_id, file_path=None):
    bot = telegram.Bot(token=tg_token)
    
    if not file_path:
        directory = os.path.join('images')
        file_paths = [os.path.join(directory, filename) for filename in os.listdir(directory)]
        file_path = random.choice(file_paths)
    
    logger.info(f'Sending photo: {file_path}')
    
    with open(file_path, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file)