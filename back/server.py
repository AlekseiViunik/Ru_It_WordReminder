import os
import random
import requests

from dotenv import load_dotenv

class Server:
    def __init__(self):
        load_dotenv()
        self.endpoint = os.getenv('ENDPOINT')
        self.key = os.getenv('YANDEX_SECRET')
        self.current_word = ''
        self.full_endpoint = ''

    def generate_endpoint(self):
        with open("src/txtfiles/rwords.txt", "r", encoding="utf-8") as file:
            words = file.readlines()
            self.current_word = random.choice(words).strip()

        # Construct the full endpoint URL
        self.full_endpoint = f"{self.endpoint}?key={self.key}&lang=ru-it&text={self.current_word}"
        return self.full_endpoint

    def send_call(self):
        ydx_endpoint = self.generate_endpoint()
        ydx_response = requests.get(ydx_endpoint)
        return [ydx_response.json()['def'][0]['text'], ydx_response.json()['def'][0]['tr'][0]['text']]


if __name__ == '__main__':
    server = Server()
    response = server.send_call()
    print(response)