from urllib.request import urlopen

# constanten: hostname van de server en definitie van de knop
hostname='192.168.42.2:5000' # vul hier de juiste hostname en poort in

# hulpfunctie voor sturen van een bericht naar de server
#    het antwoord wordt simpelweg geprint
def httpconnect(action):
    url='http://{}/{}'.format(hostname,action)
    try:
        print(urlopen(url).read().decode())
    except:
        print("Verbinding naar {} kon niet gemaakt worden".format(url))
        exit()

# actie voor ingedrukte knop (voor gebruik met gpiozero geen argument)
def knopin():
    httpconnect('knopin')

# actie voor losgelaten knop (voor gebruik met gpiozero geen argument)
def knopuit():
    httpconnect('knopuit')

# klaar voor gebruik, open de basis URL
httpconnect('')

# blijf oneindig deze lus maken, waarbij input gelezen wordt
#     en de functie knopin() aangeroepen bij invoer van '+' (gevolgd door enter)
#     en de functie knopuit() bij invoer van '-' (gevolgd door enter)
while True:
    invoer=input()
    if invoer=='+':
        knopin()
    elif invoer=='-':
        knopuit()
    # overige invoer wordt genegeerd