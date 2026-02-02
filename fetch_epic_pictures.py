import os
import requests
from datetime import datetime
from dotenv import load_dotenv

from image_downloader import download_images


EPIC_API_URL = 'https://api.nasa.gov/EPIC/api/natural/images'


def fetch_epic_metadata(api_key):
    response = requests.get(
        EPIC_API_URL,
        params={'api_key': api_key},
        timeout=10
    )
    response.raise_for_status()
    return response.json()


def build_epic_image_url(image_name, date_str, api_key):
    date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

    return (
        f'https://api.nasa.gov/EPIC/archive/natural/'
        f'{date.year}/{date.month:02d}/{date.day:02d}/'
        f'png/{image_name}.png'
        f'?api_key={api_key}'
    )


def get_epic_image_urls(epic_items, limit=10, api_key=None):
    image_urls = []

    for item in epic_items[:limit]:
        image_url = build_epic_image_url(
            item['image'],
            item['date'],
            api_key
        )
        image_urls.append(image_url)

    return image_urls


def main():
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']

    try:
        epic_items = fetch_epic_metadata(api_key)
        image_urls = get_epic_image_urls(epic_items, limit=10, api_key=api_key)

        download_images(
            image_urls=image_urls,
            images_dir='NASA/epic',
            prefix='epic'
        )

    except requests.exceptions.RequestException as error:
        print('Ошибка при работе с NASA EPIC API:')
        print(error)


if __name__ == '__main__':
    main()
