import requests
from pathlib import Path
import os
from dotenv import load_dotenv
import datetime 


def fetch_nasa_epic(url, payload):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    
    images = response.json()[:10]
    for index, image in enumerate(images, start=1):
        name = image['image']
        date = image['date']
        date = datetime.datetime.fromisoformat(date)
        formatted_date = date.strftime("%Y/%m/%d")
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{name}.png'
        image_response = requests.get(image_url, params=payload)
        image_response.raise_for_status()
        
        with open(f'images/nasa_epic_{index}.png', 'wb') as file:
            file.write(image_response.content)
            
            
def main():
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    
    Path("images").mkdir(parents=True, exist_ok=True)
    
    payload_epic = {'api_key': nasa_token}
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural'
    fetch_nasa_epic(nasa_epic_url, payload_epic)
       

if __name__ == '__main__':
    main()