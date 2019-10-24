import sqlite3, socket, sys, os, warnings

file = sqlite3.connect("pihole-FTL.db")
cursor = file.cursor()



cursor.execute("SELECT * FROM queries")
#0 ID, 1 timestamp, 2 type, 3 status, 4 domain, 5 client, 6 forward

data = cursor.fetchall()
for tab in data:
    ID = tab[0]
    timestamp = tab[1]
    typ = tab[2]
    status = tab[3]
    domain = tab[4]
    client = tab[5]
    forward = tab[6]
    #print(ID)
    """if client == "192.168.0.27":
        print(domain)
"""
    if domain.find("lookfor") != -1:
        print(domain)
        print(client)
        try:
            clientname = socket.gethostbyaddr(client)
            print(clientname)
        except:
            print("Couldn't get hostname for "+client)
        