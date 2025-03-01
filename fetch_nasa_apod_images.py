import requests
from pathlib import Path
import os
from dotenv import load_dotenv
import get_file_extension


def fetch_nasa_apod(url, payload):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    
    for index, image in enumerate(response.json(), start=1):
        image_response = requests.get(image['url'])
        image_response.raise_for_status()
        
        extension = get_file_extension.get_file_extension(image['url'])
        
        with open(f'images/nasa_apod_{index}{extension}', 'wb') as file:
            file.write(image_response.content)


def main():
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    
    Path("images").mkdir(parents=True, exist_ok=True)
    
    payload_apod = {'api_key': nasa_token, 'count': '30'}
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    fetch_nasa_apod(nasa_apod_url, payload_apod)
    
    
if __name__ == '__main__':
    main()