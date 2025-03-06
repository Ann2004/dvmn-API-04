import requests
import get_file_extension


def download_and_save_image(image_url, index, name, payload=None):
    image_response = requests.get(image_url, params=payload)
    image_response.raise_for_status()
        
    extension = get_file_extension.get_file_extension(image_url)
        
    with open(f'images/{name}{index}{extension}', 'wb') as file:
        file.write(image_response.content)