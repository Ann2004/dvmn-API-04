import os
import random


def get_downloaded_files(path):
    directory = os.path.join(path)
    file_paths = [os.path.join(directory, filename) for filename in os.listdir(directory)]
    file_path = random.choice(file_paths)
    return file_path