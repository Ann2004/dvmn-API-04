import argparse
from pathlib import Path
from telegram_bot.tg_bot import send_photo_to_chat
import os
import time
import random


def main():
    delay_hours = 4
    
    parser = argparse.ArgumentParser(description='Post photos to Telegram')
    parser.add_argument('-H', '--hours', help='publication frequency - number delay hours', type=int)
    args = parser.parse_args()
    if args.hours:
        delay_hours = args.hours
    
    directory = Path('images')
    file_paths = [os.path.join(directory, filename) for filename in os.listdir(directory)]  
    while True:
        for file_path in file_paths:
            print(file_path)
            send_photo_to_chat(file_path)
            time.sleep(delay_hours * 3600)
        random.shuffle(file_paths)
            

if __name__ == '__main__':
    main()