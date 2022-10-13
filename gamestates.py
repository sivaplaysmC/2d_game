import pygame













class GameState :
    def __init__(self  , Game) :
        self.color = "blue"
        self.Game = Game
        self.environment : "pygame.Surface" = self.Game.environment
    def main(self):
        self.environment.fill(self.color)


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
        self.environment : "pygame.Surface" = self.Game.environment
    def update(self) :
        self.Game.environment.fill((100,100,100))


class basic(GameState):
    vec = pygame.Vector2
    def __init__(self , Game) :
        super().__init__(Game)
        self.name = "basic"
        self.environment : "pygame.Surface" = self.Game.environment
    def update(self) :
        self.environment.fill("white")
        self.Game.player1.move(self.Game.dt)
        self.Game.player2.move(self.Game.dt)
        for i in self.Game.platforms :
            PLATFORM = pygame.Surface((i.width , i.height))
            PLATFORM.fill(i.color)
            self.environment.blit(PLATFORM , (i.rect.x , i.rect.y))
        PLAYER_1_IMAGE = pygame.Surface((30,30))
        PLAYER_1_IMAGE.fill(self.Game.player1.color)
        PLAYER_2_IMAGE = pygame.Surface((30,30))
        PLAYER_2_IMAGE.fill(self.Game.player2.color)
        self.environment.blit(PLAYER_1_IMAGE , (self.Game.player1.rect.x , self.Game.player1.rect.y))
        self.environment.blit(PLAYER_2_IMAGE , (self.Game.player2.rect.x , self.Game.player2.rect.y))
