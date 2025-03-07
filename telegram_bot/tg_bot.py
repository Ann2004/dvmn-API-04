import telegram
import logging
from get_downloaded_files import get_downloaded_files


logger = logging.getLogger('tg_bot')


def send_photo_to_chat(tg_token, chat_id, file_path=None):
    bot = telegram.Bot(token=tg_token)
    
    if not file_path:
        file_path = get_downloaded_files('images')
    
    logger.info(f'Sending photo: {file_path}')
    
    with open(file_path, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file)