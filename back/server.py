import json
import os
import random


class Server:

    def send_call(self):
        with open('src/txtfiles/translations.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            ru_word = random.choice(list(data.keys()))
            it_word = data[ru_word]
            return [ru_word, it_word]

if __name__ == '__main__':
    server = Server()
    response = server.send_call()
    print(response)