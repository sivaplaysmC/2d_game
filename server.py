import socket
from socket import SOCK_STREAM as SS , AF_INET as AA
from pickle import loads as ls , dumps as ds
from _thread import start_new_thread as snt
from data_parcel import DataParcel
from reading_json import rect_list

from port import p

from gserver import Game

s = socket.socket(AA , SS)
s.bind(p)
s.listen(3)
addresses = list()


##events = list()
clients = [ None , None ]

game = Game(rect_list)

def thred(conn : socket.socket , Id ) :
    print(Id)
    fh = open("log.txt" , "w")
    conn.send(ds(Id))
    while 1 :
        data = ls(conn.recv(10240))
        if Id == 0 :
            game.player1 = data.player1
        else :
            game.player2 = data.player1

        if Id == 0 :
            parcel = DataParcel(game)
            conn.send(ds(parcel))

        if Id == 1 :
            parcel = DataParcel(game)
            parcel.player1 , parcel.player2 = parcel.player2 , parcel.player1
            conn.send(ds(parcel))


cur_id = 0

def mainloop() :
    global cur_id
    while len(addresses) < 2 :
        print('waiting to Accept ')
        c,a = s.accept()
        addresses.append(a)
        snt(thred , (c , cur_id))
        cur_id += 1
    game.mainloop()


mainloop()
