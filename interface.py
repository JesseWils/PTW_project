from flask import Flask
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

def read_container():
    global newlist
    c.execute("SELECT * FROM container WHERE vuilnisniveau >= 85")
    abc = (c.fetchall())
    newlist = []
    for item in abc:
        newlist.append([item[0], item[1], item[2], item[3]])
    return newlist

def read_all_container():
    global newlistall
    c.execute("SELECT * FROM container WHERE vuilnisniveau >= 0")
    abc = (c.fetchall())
    newlistall = []
    for item in abc:
        newlistall.append([item[0], item[1], item[2], item[3]])
    return newlistall

def flask_text_maker():
    global tekst_compleet, newlist
    flasktext = 'De volgende containers zijn bijna vol: <br/> <br/>'
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

def flask_text_maker_all():
    global tekst_compleet_all, newlistall
    flasktext = 'De volgende containers zijn bijna vol: <br/> <br/>'
    formatgedoe = []
    for item in newlistall:
        flasktext += 'container nr. {} op verzamellocatie {} zit {}% vol<br/> Container niveau is het laats geupdate op: {}<br/> <br/>'
    nummer = 0
    for item in newlistall:
        formatgedoe.append(newlistall[nummer][0])
        formatgedoe.append(newlistall[nummer][2])
        formatgedoe.append(newlistall[nummer][1])
        formatgedoe.append(newlistall[nummer][3])
        nummer += 1
    tekst_compleet_all = flasktext.format(*formatgedoe)


read_container()
flask_text_maker()
read_all_container()
flask_text_maker_all()


app = Flask(__name__)


@app.route("/")
def hello():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    c.execute("SELECT * FROM container WHERE vuilnisniveau >= 85")
    abc = (c.fetchall())
    newlist = []
    for item in abc:
        newlist.append([item[0], item[1], item[2], item[3]])

    flasktext = 'De volgende containers zijn bijna vol: <br/> <br/>'
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


    return tekst_compleet

@app.route("/allecontainers")
def hello2():
    global tekst_compleet_all
    return tekst_compleet_all



if __name__ == "__main__":
    app.run(host= '0.0.0.0')
