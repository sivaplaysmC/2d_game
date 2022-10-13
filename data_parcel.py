import pickle
import pygame

class DataParcel :
    def __init__(self , Game) -> None:
        pass
        self.Game = Game
    def MakeParcel(self) :
        platforms = self.Game.platforms
        players = self.Game.players
        data = {'players' : players , 'platforms' : platforms}
        return pickle.dumps(data)
