from flask import Flask
import time





app = Flask(__name__)


@app.route("/")
def hello():
    while True:
        try:
            with open('nieuwemeting.txt', 'r') as file:
                text = file.readline()
            return text
        except FileNotFoundError:
            time.sleep(3)



if __name__ == "__main__":
    app.run(host= '0.0.0.0')
