import argparse
import requests

from common import download_images


def fetch_spacex_images(launch_id=None):
    if launch_id:
        url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    else:
        url = 'https://api.spacexdata.com/v5/launches/latest'

    response = requests.get(url)
    response.raise_for_status()
    launch_data = response.json()
    return launch_data['links']['flickr']['original']


def main():
    parser = argparse.ArgumentParser(
        description="Скачивает фотографии SpaceX по ID запуска."
    )
    parser.add_argument(
        'launch_id',
        nargs='?',
        default=None,
        help='ID запуска SpaceX'
    )
    args = parser.parse_args()

    image_urls = fetch_spacex_images(args.launch_id)

    if not image_urls:
        print("Нет изображений для этого запуска.")
        return

    download_images(image_urls, 'Space X', prefix='spacex')


if __name__ == '__main__':
    main()
