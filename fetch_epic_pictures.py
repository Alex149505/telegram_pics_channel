import os
import requests
from datetime import datetime
from dotenv import load_dotenv

from common import download_images


EPIC_API_URL = 'https://api.nasa.gov/EPIC/api/natural/images'


def fetch_epic_metadata(api_key):
    try:
        response = requests.get(
            EPIC_API_URL,
            params={'api_key': api_key},
            timeout=10
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as error:
        print('Ошибка при запросе к NASA EPIC API:')
        print(error)
        return []


def build_epic_image_url(image_name, date_str, api_key):
    date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

    return (
        f'https://api.nasa.gov/EPIC/archive/natural/'
        f'{date.year}/{date.month:02d}/{date.day:02d}/'
        f'png/{image_name}.png'
        f'?api_key={api_key}'
    )


def get_epic_image_urls(epic_items, limit=10):
    image_urls = []

    for item in epic_items[:limit]:
        image_url = build_epic_image_url(
            item['image'],
            item['date']
        )
        image_urls.append(image_url)

    return image_urls


def main():
    load_dotenv()
    api_key = os.environ['API_KEY']

    epic_items = fetch_epic_metadata(api_key)
    if not epic_items:
        print('Не удалось получить данные EPIC')
        return

    image_urls = get_epic_image_urls(epic_items, limit=10)

    download_images(
        image_urls=image_urls,
        images_dir='NASA/epic',
        prefix='epic'
    )


if __name__ == '__main__':
    main()
