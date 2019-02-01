import sqlite3


conn = sqlite3.connect('PTWproject.db') #voer hier de naam van de database in
c = conn.cursor()
#als ze nog niet bestaan worden hier de tables aangemaakt.
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
    #functie om container toe te voegen
    with conn:
        c.execute("INSERT INTO container VALUES (?, ?, ?, ?)", (newcontainer[0], newcontainer[1], newcontainer[2], newcontainer[3]))

def delete_container(containerid):
    #functie om container te verwijderen
    with conn:
        c.execute("DELETE FROM container WHERE containerID = (?)", (containerid,))

def update_vuilnisniveau(containerid, newniveau, newdate):
    #functie om container te updaten
    with conn:
        c.execute("UPDATE container SET vuilnisniveau = (?), datumLaatsteUpdate = (?) WHERE containerID = (?)", (newniveau, newdate, containerid))
    print('geupdate')

def read_container():
    # Om tables te lezen
    c.execute("SELECT containerID FROM container WHERE vuilnisniveau >= 80")

c.execute("INSERT INTO container VALUES (1, 0, 1, 'Thu 31 January 16:01:08')")
c.execute("INSERT INTO container VALUES (2, 43, 1, 'Thu 31 January 14:04:45')")
c.execute("INSERT INTO container VALUES (3, 83, 1, 'Wed 30 January 11:34:23')")
# c.execute("SELECT * FROM container WHERE vuilnisniveau >= 50")

#handmatig nieuwe container toevoegen
new_container3 = [4, 89, 1, 'Thu 31 Januari 15:45:56']
new_container4 = [5, 34, 2, 'Thu 31 Januari 11:15:37']
new_container5 = [6, 12, 2, 'Thu 31 Januari 03:39:51']
new_container6 = [7, 65, 2, 'Thu 31 Januari 13:38:42']
new_container7 = [8, 80, 3, 'Thu 31 Januari 15:13:45']
new_container8 = [9, 99, 3, 'Thu 31 Januari 12:47:12']

add_container(new_container3)
add_container(new_container4)
add_container(new_container5)
add_container(new_container6)
add_container(new_container7)
add_container(new_container8)


# c.execute("SELECT * FROM container")
# print(c.fetchall())


# update_vuilnisniveau(1, 90, 'eoaghuipaehus[')
# c.execute("SELECT * FROM container")
# print(c.fetchall())

#commit wijzigingen
conn.commit()

#sluit database
conn.close()
