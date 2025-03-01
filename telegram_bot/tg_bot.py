import telegram
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    
    chat_id = '@cosmosDvmn'
    bot.send_document(chat_id=chat_id, document='https://python-telegram-bot.org/static/testfiles/telegram.gif')


if __name__ == '__main__':
    main()
    