import os
import random

from dotenv import load_dotenv

class Server:
    def __init__(self):
        load_dotenv()
        self.endpoint = os.getenv('ENDPOINT')
        self.key = os.getenv('YANDEX_SECRET')

    def generate_endpoint(self):
        with open("../src/txtfiles/rwords.txt", "r", encoding="utf-8") as file:
            words = file.readlines()
            random_word = random.choice(words).strip()

        # Construct the full endpoint URL
        full_endpoint = f"{self.endpoint}?key={self.key}&lang=ru-it&text={random_word}"
        return full_endpoint

    def sendcall(self):
        # TODO: add logic to send call to Yandex endpoint to get the word's translation
        pass


if __name__ == '__main__':
    server = Server()
    path = server.generate_endpoint()
    print(path)