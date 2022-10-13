import socket
from socket import SOCK_STREAM as SS , AF_INET as AA
from pickle import loads as ls , dumps as ds
from _thread import start_new_thread as snt

s = socket.socket(AA , SS)
s.bind(('localhost' , 9090))
s.listen(3)
addresses = list()


##events = list()
clients = [ , None ]

def thred(conn : socket.socket , Id ) :
    print(Id)
    fh = open("log.txt" , "w")
    conn.send(ds(Id))
    while 1 :
        data = ls(conn.recv(1024))
        events[Id] = data
        if events[0] or events[1] :
            fh.write(str(events) + "\n")
            fh.flush()
        conn.send(ds(events))

cur_id = 0

def mainloop() :
    global cur_id
    while len(addresses) < 2 :
        c,a = s.accept()
        addresses.append(a)
        snt(thred , (c , cur_id))
        cur_id += 1

    player1 = clients[0].player1 , player2 = clients[1].player1



mainloop()
