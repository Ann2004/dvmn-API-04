import argparse
from pathlib import Path
from telegram_bot.tg_bot import send_photo_to_chat
import os
import time
import random
from dotenv import load_dotenv


def main():
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    
    parser = argparse.ArgumentParser(description='Post photos to Telegram')
    parser.add_argument('-H', '--hours', help='publication frequency - number delay hours', type=int, default=4)
    args = parser.parse_args()
    
    directory = Path('images')
    file_paths = [os.path.join(directory, filename) for filename in os.listdir(directory)]  
    while True:
        for file_path in file_paths:
            send_photo_to_chat(tg_token, chat_id, file_path)
            time.sleep(args.hours * 3600)
        random.shuffle(file_paths)
            

if __name__ == '__main__':
    main()