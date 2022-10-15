import pickle
from data_parcel import DataParcel
from time import time
import pygame
from reading_json import rect_list
from entity import Platform,  Entity
from gamestates import Main_menu, Pause_menu, basic


class Stack:
    def __init__(self):
        self.stack = list()
        pass
    def pop(self) :
        self.stack.pop()
    def add(self,item):
        self.stack.append(item)
    def peek(self):
        return self.stack[-1]


class Res:
    def __init__(self , *args) -> None:
        self.x , self.y = args


class Game:
    environment_surface_res = Res(1280,720)
    display_surface_res = Res(1408 , 736)
    def __init__(self , rect_list:list) :
        self.game_state_stack = Stack()
        self.environment_surface_res = Res(1280,720)
        self.display_surface_res = Res(1408 , 736)
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.prev = 0
        self.rect_list = rect_list

        self.player1 = Entity("blue")
        self.player1.name = "Player1"
        self.player1.other_player_name = "Player2"

        self.player2 = Entity("red")
        self.player2.name = "Player2"
        self.player2.other_player_name = "Player1"
        self.player2.jump_key = pygame.K_UP


        self.players = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()


        self.players.add(self.player1 , self.player2)


        for i in self.rect_list :
            self.platforms.add(Platform(i.x , i.y  , i.w , i.h ,"black"))

        self.player1.other_player = self.player2
        self.player2.other_player = self.player1
        self.player1.collidelist.add(*self.platforms.sprites() , self.player2)
        self.player2.collidelist.add(*self.platforms.sprites() , self.player1)


        self.running = True
        self.game_state_stack.add(Main_menu(self))
    def dt_clock(self) :
        self.now = time()
        self.dt =  self.now - self.prev
        self.prev = self.now
    def get_input(self) :
        for self.event in pygame.event.get() :
            if self.event.type == pygame.QUIT :
                self.running = False

            if self.event.type == pygame.KEYDOWN :
                if self.event.key == pygame.K_RETURN :
                    if self.game_state_stack.peek().name == "Main" :
                        self.game_state_stack.add(basic(self))
                if self.event.key == pygame.K_ESCAPE :
                    if self.game_state_stack.peek().name != "Pause" :
                        self.game_state_stack.add(Pause_menu(self))
                    else :
                        self.game_state_stack.pop()
                if self.event.key == pygame.K_RIGHT :
                    self.player1.actions["right"] = True

                if self.event.key == pygame.K_UP :
                    self.player1.actions["up"] = True
                if self.event.key == pygame.K_LEFT :
                    self.player1.actions["left"] = True
            if self.event.type == pygame.KEYUP :
                if self.event.key == pygame.K_RIGHT :
                    self.player1.actions["right"] = False
                if self.event.key == pygame.K_LEFT :
                    self.player1.actions["left"] = False
                if self.event.key == pygame.K_UP :
                    self.player1.actions["up"] = False
    def update(self) :
        self.game_state_stack.peek().update()

    def draw(self) :
        ENVIRONMENT.fill('teal')
        for i in self.platforms :
            PLATFORM = pygame.Surface((i.width , i.height))
            PLATFORM.fill(i.color)
            ENVIRONMENT.blit(PLATFORM , (i.rect.x , i.rect.y))
        PLAYER_1_IMAGE = pygame.Surface((30,30))
        PLAYER_1_IMAGE.fill(self.player1.color)
        PLAYER_2_IMAGE = pygame.Surface((30,30))
        PLAYER_2_IMAGE.fill(self.player2.color)
        ENVIRONMENT.blit(PLAYER_1_IMAGE , (self.player1.rect.x , self.player1.rect.y))
        ENVIRONMENT.blit(PLAYER_2_IMAGE , (self.player2.rect.x , self.player2.rect.y))
        DISPLAY.blit(pygame.transform.scale(ENVIRONMENT , (self.display_surface_res.x , self.display_surface_res.y)) , (0,0) )
        pygame.display.flip()
    def mainloop(self) :
        while self.running :
            self.fps = self.clock.get_fps()
            self.dt = self.clock.tick(60) / 1000
            self.get_input()
            self.update()
            self.draw()

                ### TODO Send the above Parcel to the server and get back data and intergrate it here

            # print(self.player1.name ,self.player1.other_player_name )
            # print(self.player2.name ,self.player2.other_player_name )

ENVIRONMENT =  pygame.Surface(( Game.display_surface_res.x , Game.display_surface_res.y  ))
DISPLAY = pygame.display.set_mode((Game.display_surface_res.x , Game.display_surface_res.y))

if __name__ == '__main__':

    game = Game(rect_list)

    game.mainloop()
    # g = Game()
