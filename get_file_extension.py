from urllib.parse import urlsplit, unquote
from os.path import split, splitext

def get_file_extension(url):
    decoded_url = unquote(url)
    image_path = urlsplit(decoded_url).path
    file_name = split(image_path)[1]
    extension = splitext(file_name)[1]
    return extension