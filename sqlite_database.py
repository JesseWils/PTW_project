import sqlite3
import time


conn = sqlite3.connect('test.db')

c = conn.cursor()

try:
    c.execute("""CREATE TABLE inzamellocatie (
                locatieID INTEGER PRIMARY KEY,
                adres TEXT
                )""")

    c.execute("""CREATE TABLE container (
                containerID INTEGER PRIMARY KEY,
                vuilnisniveau INTEGER,
                locatieID INTEGER,
                datumLaatsteUpdate TEXT,
                FOREIGN KEY(locatieID) REFERENCES inzamellocatie(locatieID)
                )""")

    c.execute("""CREATE TABLE gemeente (
                gemeenteID INTEGER PRIMARY KEY,
                gemeentenaam TEXT
                )""")

    c.execute("""CREATE TABLE bewoner (
                burgerservicennummer INTEGER PRIMARY KEY,
                naam TEXT,
                adres TEXT
                )""")
except sqlite3.OperationalError:
    print('tables already exist')


def add_container(newcontainer):
    with conn:
        c.execute("INSERT INTO container VALUES (?, ?, ?, ?)", (newcontainer[0], newcontainer[1], newcontainer[2], newcontainer[3]))

def delete_container(containerid):
    with conn:
        c.execute("DELETE FROM container WHERE containerID = (?)", (containerid,))

def update_vuilnisniveau(containerid, newniveau, newdate):
    with conn:
        c.execute("UPDATE container SET vuilnisniveau = (?), datumLaatsteUpdate = (?) WHERE containerID = (?)", (newniveau, newdate, containerid))

def read_container():
    c.execute("SELECT containerID FROM container WHERE vuilnisniveau >= 80")

# c.execute("INSERT INTO container VALUES (0001, 98, 1, 'maandag blah blah')")
# c.execute("INSERT INTO container VALUES (0002, 43, 1, 'dinsdag blah blah')")
# c.execute("INSERT INTO container VALUES (0003, 83, 1, 'zaterdag blah blah')")
# c.execute("SELECT * FROM container WHERE vuilnisniveau >= 50")

# new_container3 = [4, 0, 1, 'dins']
# new_container4 = [5, 0, 2, 'woens']
# new_container5 = [6, 0, 2, 'februari']
# new_container6 = [7, 0, 2, 'december']
# new_container7 = [8, 80, 3, '3-6-2019']
# new_container8 = [9, 99, 3, 'vandaag']

# add_container(new_container3)
# add_container(new_container4)
# add_container(new_container5)
# add_container(new_container6)
# add_container(new_container7)
# add_container(new_container8)
# delete_container(2)

c.execute("SELECT * FROM container")
print(c.fetchall())

c.execute("SELECT * FROM container WHERE vuilnisniveau >= 80")
print(c.fetchall())

update_vuilnisniveau(1, 55, 'zondag blah blah blah')
c.execute("SELECT * FROM container")
print(c.fetchall())


conn.commit()


def newdata():
    global list
    while True:
        try: # Hier probeert het programma 'sensorcheck.txt' te openen. Als dit niet lukt probeert het programma het opnieuw.
            #os.system('ls /home/pi/share') # Update de directory
            with open('nieuwemeting.txt', 'r+') as myfile:
                newdata = myfile.read().split(',')

            to_replace_containerID = str(newdata[0])
            to_replace_garbagelevel = str(newdata[1])
            datum = str(newdata[2])
            to_replace_containerID = int(to_replace_containerID[1:])
            to_replace_garbagelevel = int(to_replace_garbagelevel[1:])
            datum = datum[2:-2]
            list = [to_replace_containerID, to_replace_garbagelevel, datum]
            print(list)
            time.sleep(900)     #900 seconde = kwartier
    #       os.remove('nieuwemeting.txt')

        except FileNotFoundError:
            time.sleep(900)
            print('Niks')

newdata()

update_vuilnisniveau(list[0], list[1], list[2])

conn.close()