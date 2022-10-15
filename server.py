import socket
from socket import SOCK_STREAM as SS , AF_INET as AA
from pickle import loads as ls , dumps as ds
from _thread import start_new_thread as snt

from port import p

from gserver import Game

s = socket.socket(AA , SS)
s.bind(p)
s.listen(3)
addresses = list()


##events = list()
clients = [ None , None ]

def thred(conn : socket.socket , Id ) :
    print(Id)
    fh = open("log.txt" , "w")
    conn.send(ds(Id))
    while 1 :
        data = ls(conn.recv(10240))
        clients[Id] = data
        conn.send(ds( clients[Id - 1] ))


cur_id = 0

def mainloop() :
    global cur_id
    while len(addresses) < 2 :
        print('waiting to Accept ')
        c,a = s.accept()
        addresses.append(a)
        snt(thred , (c , cur_id))
        cur_id += 1


mainloop()
