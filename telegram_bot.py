import os
from dotenv import load_dotenv
from telegram import Bot


def send_message(token):
    bot = Bot(token=token)

    chat_id = -1003873120271
    return bot.send_message(chat_id=chat_id, text="test")


def main():
    load_dotenv()

    token = os.getenv('TOKEN')
    if not token:
        raise RuntimeError('TOKEN не найден в .env')

    send_message(token)


if __name__ == '__main__':
    main()
