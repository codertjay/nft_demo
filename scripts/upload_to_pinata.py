# from decouple import config
from pathlib import Path

import requests

PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
# Change this filepath
filepath = "./img/pug.png"
filename = filepath.split("/")[-1:][0]
headers = {
    'pinata_api_key': "d88bd1537f59b24bc888",
    'pinata_secret_api_key': "8d042d02f38442573e98f5c22cc8e03a020eaa3b330191baedc961eb650096a5"
}


def main():
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, image_binary)},
            headers=headers,
        )
        print(response.json())
