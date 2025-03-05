# Automated posting of space photos in Telegram

Get photos from NASA and Spacex and automate your Telegram posting if you don't have time to run a channel yourself.


## What is included:
- Downloading SpaceX images from the last launch or any other lauch by id - [fetch_spacex_images.py](https://github.com/Ann2004/dvmn-API-04/blob/main/fetch_spacex_images.py)
- Downloading NASA EPIC and APOD images - [fetch_nasa_epic_images.py](https://github.com/Ann2004/dvmn-API-04/blob/main/fetch_nasa_epic_images.py), [fetch_nasa_apod_images.py](https://github.com/Ann2004/dvmn-API-04/blob/main/fetch_nasa_apod_images.py)
- Automated posting of downloaded images to Telegram channel once in several hours (the number of hours can be changed) - [post_photos_to_telegram.py](https://github.com/Ann2004/dvmn-API-04/blob/main/post_photos_to_telegram.py)
- Publication of the specified or random image to Telegram channel - [telegram_bot/tg_bot.py](https://github.com/Ann2004/dvmn-API-04/blob/main/telegram_bot/tg_bot.py)


## Installation

Create a `.env` file in the project directory and add your NASA token, Telegram bot token and chat id:
```
NASA_TOKEN=your_nasa_access_token
TG_TOKEN=your_tg_access_token
TG_CHAT_ID=your_chat_id
```

- To use the NASA API, you need an access token. [Generate API Key](https://api.nasa.gov/).
- Create your Telegram bot using [BotFather](https://telegram.me/BotFather) and get the bot's API token.
- The chat_id of a channel is a link to it, for example: @dvmn_flood. You also need to make the bot a channel admin.

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```


## Example usage


### Download SpaceX images:
Run the script from the command line, providing the launch id as an argument. The pictures will be downloaded to the 'images' directory.
```
python fetch_spacex_images.py -id <launch_id>
```
- If no argument is specified, the images of the last launch will be downloaded.

You can find the id's of the different launches [here](https://api.spacexdata.com/v5/launches).


### Download NASA EPIC (Earth Polychromatic Imaging Camera) and APOD (Astronomy Picture of the Day) images:
Run the scripts from the command line to download pictures to the 'images' directory.
```
python fetch_nasa_epic_images.py
```
```
python fetch_nasa_epod_images.py
```


### Automated posting of downloaded images to Telegram channel once in several hours:
Photos are posted from the 'images' directory every few hours. Publication frequency - number of delay hours can be changed. Run the script from the command line, providing the number of hours as an argument.
```
python post_photos_to_telegram.py -H <number_of_hours>
```
- If no argument is specified, by default photos will be posted one every 4 hours.


### Post random or specified image to Telegram channel:
Run the script from the command line to post random photo to Telegram.
```
python .\telegram_bot\tg_bot.py
```
- In the script when calling the send_photo_to_chat() function, specify the path to the image as an argument if you need to send a specific photo.


## Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
