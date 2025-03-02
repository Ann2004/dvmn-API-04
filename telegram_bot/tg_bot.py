import telegram
import os
from dotenv import load_dotenv
import random


def send_photo_to_chat(file_path=None):
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    
    chat_id = os.environ['TG_CHAT_ID']
    
    if file_path is None:
        directory = os.path.join('images')
        file_paths = [os.path.join(directory, filename) for filename in os.listdir(directory)]
        file_path = random.choice(file_paths)
           
    bot.send_document(chat_id=chat_id, document=open(file_path, 'rb')) 

    
if __name__ == "__main__":
    send_photo_to_chat()