# import sqlite3
#
# conn = sqlite3.connect('test.db')
#
# c = conn.cursor()
#
#
# def read_container():
#     c.execute("SELECT * FROM container WHERE vuilnisniveau >= 50")
#     abc = (c.fetchall())
#     newlist = []
#     print(abc)
#     print(abc[0][0])
#     for item in abc:
#         print(item[0])
#         newlist.append(item[0])
#     print(newlist)
#
#
#     # print(abc[3][0])
#
# read_container()

testlist = ['aap','noot',3,'mies',5,6,7,8,9]
flasktext = ''
formatgedoe = []

def flask_text_maker():
    global flasktext, formatgedoe
    for item in testlist:
        flasktext += '{} %<br/>'
    print(flasktext)
    nummer = 0
    for item in testlist:
        formatgedoe.append(testlist[nummer])
        nummer += 1
    print(formatgedoe)
    # str1 = ''.join(str(e) for e in formatgedoe)
    # print(str1)
    # variable = flasktext,'.',format,format()
    varia = flasktext.format(*formatgedoe)
    print(str(varia))
flask_text_maker()

