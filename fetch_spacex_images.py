import requests
from pathlib import Path
import argparse


def fetch_spacex_last_launch(url):
    response = requests.get(url)
    response.raise_for_status()
    image_urls = response.json()['links']['flickr']['original']
    
    for index, image_url in enumerate(image_urls, start=1):
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        with open(f'images/spacex{index}.jpg', 'wb') as file:
            file.write(image_response.content)
        

def main():
    parser = argparse.ArgumentParser(description='download photos from SpaceX')
    parser.add_argument('-id', '--launch_id', help='Launch ID')
    args = parser.parse_args()
    launch_id = args.launch_id
    
    Path("images").mkdir(parents=True, exist_ok=True)
    
    if launch_id:
        spacex_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    else:
        spacex_url = 'https://api.spacexdata.com/v5/launches/latest'
    
    fetch_spacex_last_launch(spacex_url)
    
    
if __name__ == '__main__':
    main()
    
#6243adcaaf52800c6e919254 - launch id
#61fc0203e0dc5662b76489a8  - launch id