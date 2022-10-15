from os import pwrite
from time import sleep
import pygame
import socket
from _thread import start_new_thread as start_thread
from pickle import loads as ls , dumps as ds
from data_parcel import DataParcel
from entity import Entity
from reading_json import rect_list
from gcli import Game
from port import p



sock = socket.socket()
events = []
game = Game(rect_list)
sock.connect(p)

def speak() :
    sleep(2.0)
    print('Hi There')
    Id :int = ls(sock.recv(1024))
    while 1 :
        parcel = game.player1
        sock.send(ds(parcel))
        parcel : Entity = ls(sock.recv(10240))
        game.player2 = parcel

start_thread(speak , tuple())



game.mainloop()
