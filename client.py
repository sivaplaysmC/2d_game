import pygame
import socket
from _thread import start_new_thread as start_thread
from pickle import loads as ls , dumps as ds


win = pygame.display.set_mode((500,500) , pygame.RESIZABLE)
win.fill('teal')
clock = pygame.time.Clock()

running = 1

sock = socket.socket()
events = []



def speak() :
    sock.connect(('localhost', 9090))
    Id = ls(sock.recv(1024))
    while 1 :
        print(Id)
        sock.send(ds(events))
        (ls(sock.recv(1024)))


start_thread(speak , tuple())
while running :
    events = []
    clock.tick(60)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            quit()
        if event.type == pygame.KEYDOWN :
            events.append(event.type)
    pygame.display.flip()
