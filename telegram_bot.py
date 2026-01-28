import os
import random
from dotenv import load_dotenv
from telegram import Bot


NASA_DIR = 'NASA/apod'


def send_message(token):
    bot = Bot(token=token)

    chat_id = -1003873120271
    images = os.listdir(NASA_DIR)
    image_name = random.choice(images)
    image_path = os.path.join(NASA_DIR, image_name)
    with open(image_path, 'rb') as photo:
        bot.send_photo(
            chat_id=chat_id,
            photo=photo,
        )


def main():
    load_dotenv()
    token = os.getenv('TOKEN')
    if not token:
        raise RuntimeError('TOKEN не найден в .env')

    send_message(token)


if __name__ == '__main__':
    main()
