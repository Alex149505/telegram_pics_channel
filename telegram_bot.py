import os
import time
import argparse

from dotenv import load_dotenv
from telegram import Bot


def get_all_files(files_dirs):
    files = []
    for directory in files_dirs:
        for root, _, filenames in os.walk(directory):
            for filename in sorted(filenames):
                files.append(os.path.join(root, filename))
    return files


def send_file(bot, chat_id, file_path):
    with open(file_path, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)


def publish_single_file(bot, chat_id, file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'Файл не найден: {file_path}')
    send_file(bot, chat_id, file_path)


def publish_files_forever(bot, chat_id, files_dirs):
    files = get_all_files(files_dirs)
    if not files:
        raise RuntimeError('В указанных папках нет файлов')

    idx = 0
    while True:
        send_file(bot, chat_id, files[idx])
        idx = (idx + 1) % len(files)
        time.sleep(4 * 60 * 60)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Публикация файлов в Telegram-канал'
    )
    parser.add_argument(
        '--file',
        help='Путь к конкретному файлу для публикации',
        type=str
    )
    return parser.parse_args()


def main():
    load_dotenv()
    token = os.environ['TOKEN']
    chat_id = (os.environ['CHAT_ID'])

    files_dirs = [
        'NASA/apod',
        'Space X',
        'NASA/epic',
    ]

    args = parse_arguments()
    bot = Bot(token=token)

    if args.file:
        publish_single_file(bot, chat_id, args.file)
    else:
        publish_files_forever(bot, chat_id, files_dirs)


if __name__ == '__main__':
    main()
