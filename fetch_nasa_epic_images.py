import requests
from pathlib import Path
import os
from dotenv import load_dotenv
import datetime
import download_and_save_image

NUMBER_OF_IMAGES = 10

def fetch_nasa_epic(nasa_token):
    payload = {'api_key': nasa_token}
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural'
    response = requests.get(nasa_epic_url, params=payload)
    response.raise_for_status()
    
    images = response.json()[:NUMBER_OF_IMAGES]
    for index, image in enumerate(images, start=1):
        name = image['image']
        date = image['date']
        date = datetime.datetime.fromisoformat(date)
        formatted_date = date.strftime("%Y/%m/%d")
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{name}.png'
        name = 'nasa_epic_'
        download_and_save_image.download_and_save_image(image_url, index, name, payload)
            
            
def main():
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    
    Path("images").mkdir(parents=True, exist_ok=True)
    
    fetch_nasa_epic(nasa_token)
       

if __name__ == '__main__':
    main()