import os
from dotenv import load_dotenv

class Server:
    def __init__(self, endpoint, key):
        self.endpoint = endpoint
        self.key = key

    def generate_endpoint(self):
        # TODO: add logic to generate endpoint using random word from txtfiles/rwords.txt
        pass

    def sendcall(self):
        # TODO: add logic to send call to Yandex endpoint to get the word's translation
        pass


if __name__ == '__main__':
    load_dotenv()
    key = os.getenv("YANDEX_SECRET")
    endpoint = os.getenv("ENDPOINT")
    server = Server(endpoint, key)
    print(f"Endpoint is {server.endpoint}")
    print(f"Key is {server.key}")