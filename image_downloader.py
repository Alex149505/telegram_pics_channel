import os
import requests
from urllib.parse import urlsplit, unquote


def get_file_extension(url):
    path = unquote(urlsplit(url).path)
    _, extension = os.path.splitext(path)
    return extension


def download_images(image_urls, images_dir, prefix='image'):
    os.makedirs(images_dir, exist_ok=True)

    for index, image_url in enumerate(image_urls):
        response = requests.get(image_url)
        response.raise_for_status()

        extension = get_file_extension(image_url)
        filename = f'{prefix}_{index}{extension}'
        file_path = os.path.join(images_dir, filename)

        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f'Saved {file_path}')


def main():
    pass


if __name__ == '__main__':
    main()
