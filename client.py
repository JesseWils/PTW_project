from urllib.request import urlopen
import sqlite3
import time


conn = sqlite3.connect('PTWproject.db')

c = conn.cursor()

# constanten: hostname van de server en definitie van de knop
hostname='192.168.42.1:5000' # vul hier de juiste hostname en poort in

# hulpfunctie voor sturen van een bericht naar de server
#    het antwoord wordt simpelweg geprint
def httpconnect(action):
    global nieuwe_meet_data
    url='http://{}/{}'.format(hostname,action)
    try:
        print(urlopen(url).read().decode())
        nieuwe_meet_data = urlopen(url).read().decode()
    except:
        print("Verbinding naar {} kon niet gemaakt worden".format(url))
        exit()

def update_vuilnisniveau(containerid, newniveau, newdate):
    with conn:
        #clause om data base te update met nieuwe gegevens)
        c.execute("UPDATE container SET vuilnisniveau = (?), datumLaatsteUpdate = (?) WHERE containerID = (?)",(newniveau, newdate, containerid))
    print('geupdate')

while True:
    #connect met local host van pi
    httpconnect('')
    #data wordt zo bewerkt tot een list wat gebruikt kan worden om de update uit te voeren (van list in een string naar gewoon list)
    newdata = nieuwe_meet_data.split(',')

    to_replace_containerID = str(newdata[0])
    to_replace_garbagelevel = str(newdata[1])
    datum = str(newdata[2])
    to_replace_containerID = int(to_replace_containerID[1:])
    to_replace_garbagelevel = int(to_replace_garbagelevel[1:])
    datum = datum[2:-2]
    list = [to_replace_containerID, to_replace_garbagelevel, datum]
    #update database
    update_vuilnisniveau(list[0], list[1], list[2])

    conn.commit()
    #wacht tot volgende update
    time.sleep(5)
