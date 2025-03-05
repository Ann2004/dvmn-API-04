import requests
from pathlib import Path
import argparse
import download_and_save_image


def fetch_spacex_last_launch(url):
    response = requests.get(url)
    response.raise_for_status()
    image_urls = response.json()['links']['flickr']['original']
    
    for index, image_url in enumerate(image_urls, start=1):
        name = 'spacex'
        download_and_save_image.download_and_save_image(image_url, index, name)
        

def main():
    parser = argparse.ArgumentParser(description='download photos from SpaceX')
    parser.add_argument('-id', '--launch_id', help='Launch ID', default='latest')
    args = parser.parse_args()
    launch_id = args.launch_id
    
    Path("images").mkdir(parents=True, exist_ok=True)
    
    spacex_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    
    fetch_spacex_last_launch(spacex_url)
    
    
if __name__ == '__main__':
    main()