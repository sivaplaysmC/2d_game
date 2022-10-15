import pygame













class GameState :
    def __init__(self  , Game) :
        self.color = "blue"
        self.Game = Game


class Pause_menu(GameState):
    def __init__(self , Game):
        super().__init__(Game)
        self.name = "Pause"
        self.environment : "pygame.Surface" = self.Game.environment

    def update(self) :
        self.Game.environment.fill("white")
        self.Game.environment.blit(pygame.transform.scale(pygame.image.load("pause_menu.png"), (self.Game.environment.get_width(), self.Game.environment.get_height() )), (0,0))


class Main_menu(GameState) :
    def __init__(self, Game):
        super().__init__(Game)
        self.name = "Main"
    def update(self) :
        basic.update(self)


class basic(GameState):
    vec = pygame.Vector2
    def __init__(self , Game) :
        super().__init__(Game)
        self.name = "basic"
    def update(self) :
        self.Game.player1.move(self.Game.dt)
        self.Game.player2.move(self.Game.dt)
