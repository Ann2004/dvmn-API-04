import requests
from pathlib import Path
import os
from dotenv import load_dotenv
import download_and_save_image


def fetch_nasa_apod(nasa_token, posts_amount=15):
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': nasa_token, 'count': posts_amount}
    response = requests.get(nasa_apod_url, params=payload)
    response.raise_for_status() 
    
    for index, image in enumerate(response.json(), start=1):
        name = 'nasa_apod_'
        download_and_save_image.download_and_save_image(image['url'], index, name)


def main():
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    
    Path("images").mkdir(parents=True, exist_ok=True)
    
    fetch_nasa_apod(nasa_token)
    
    
if __name__ == '__main__':
    main()