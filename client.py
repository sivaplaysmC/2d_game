from time import sleep
import pygame
import socket
from _thread import start_new_thread as start_thread
from pickle import loads as ls , dumps as ds
from reading_json import rect_list
from gcli import Game
from port import p



sock = socket.socket()
events = []
game = Game(rect_list)
sock.connect(p)

data = {'self' : game.player1 , 'other' : game.player2 }
def speak() :
    sleep(1.0)
    print('Hi There')
    Id :int = ls(sock.recv(1024))
    while 1 :
        data = {'Id' : Id , 'player1' : game.player1 , 'player2' : game.player2 , }
        sock.send(ds(data))
        data = (ls(sock.recv(10240)))
        game.player1 = data['player1']
        game.player2 = data['player2']


start_thread(speak , tuple())
game.mainloop()
