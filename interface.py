from flask import Flask
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

def read_container():
    global newlist
    c.execute("SELECT * FROM container WHERE vuilnisniveau >= 0")
    abc = (c.fetchall())
    newlist = []
    for item in abc:
        newlist.append([item[0], item[1], item[2], item[3]])
    return newlist

def flask_text_maker():
    global tekst_compleet, newlist
    flasktext = 'De volgende containers zijn bijna vol: <br/>'
    formatgedoe = []
    for item in newlist:
        flasktext += 'container nr. {} op verzamellocatie {} zit {}% vol<br/> Container niveau is het laats geupdate op: {}<br/> <br/>'
    nummer = 0
    for item in newlist:
        formatgedoe.append(newlist[nummer][0])
        formatgedoe.append(newlist[nummer][2])
        formatgedoe.append(newlist[nummer][1])
        formatgedoe.append(newlist[nummer][3])
        nummer += 1
    tekst_compleet = flasktext.format(*formatgedoe)


read_container()
flask_text_maker()


app = Flask(__name__)


@app.route("/")
def hello():
    global tekst_compleet
    return tekst_compleet


if __name__ == "__main__":
    app.run()
