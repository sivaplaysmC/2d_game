import pickle
import pygame

class DataParcel :
    def __init__(self , Game) -> None:
        self.player1 = Game.player1
        self.player2 = Game.player2
