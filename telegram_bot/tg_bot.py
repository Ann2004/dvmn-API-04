import telegram
import logging


logger = logging.getLogger('tg_bot')


def send_photo_to_chat(tg_token, chat_id, file_path):
    bot = telegram.Bot(token=tg_token)
    
    logger.info(f'Sending photo: {file_path}')
    
    with open(file_path, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file)