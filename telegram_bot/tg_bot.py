import telegram
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    
    chat_id = '@cosmosDvmn'
    bot.send_message(chat_id=chat_id, text="We are stardust.")


if __name__ == '__main__':
    main() 