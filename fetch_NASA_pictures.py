import os
import requests
from dotenv import load_dotenv

from common import download_images


URL = 'https://api.nasa.gov/planetary/apod'


def fetch_nasa_pictures(api_key):
    params = {
        'api_key': api_key,
        'count': 30
    }
    response = requests.get(URL, params=params)
    response.raise_for_status()
    return response.json()


def main():
    load_dotenv()
    api_key = os.environ['API_KEY']
    apod_items = fetch_nasa_pictures(api_key)

    image_urls = []

    for item in apod_items:
        if item.get('media_type') == 'image':
            image_urls.append(item['url'])

    download_images(
        image_urls=image_urls,
        images_dir='NASA',
        prefix='apod'
    )


if __name__ == '__main__':
    main()
