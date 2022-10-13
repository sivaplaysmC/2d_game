from time import time
import pygame
from reading_json import rect_list
# from classes_and_funcs import Entity , Platform
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
    def __init__(self , rect_list:list) :
        self.game_state_stack = Stack()
        self.environment_surface_res = Res(1280,720)
        self.display_surface_res = Res(1408 , 736)
        self.environment =  pygame.Surface((self.environment_surface_res.x , self.environment_surface_res.y))
        self.display = pygame.display.set_mode((self.display_surface_res.x , self.display_surface_res.y))
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.prev = 0
        self.rect_list = rect_list

        self.player = Entity("blue")
        self.player.name = "Player1"
        self.player.jump_key = pygame.K_UP
        self.other_player_name = "Player2"



        self.all_objects =pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()


        self.players.add(self.player)
        for i in self.rect_list :
            self.platforms.add(Platform(i.x , i.y  , i.w , i.h ,"black"))

        self.player.collidelist.add(*self.platforms.sprites())

        self.running = True
        # self.game_state_stack.add(mini(self))
        self.game_state_stack.add(Main_menu(self))



        self.cur_id = 0




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
                    self.player.actions["right"] = True

                if self.event.key == pygame.K_UP :
                    self.player.actions["up"] = True
                if self.event.key == pygame.K_LEFT :
                    self.player.actions["left"] = True
            if self.event.type == pygame.KEYUP :
                if self.event.key == pygame.K_RIGHT :
                    self.player.actions["right"] = False
                if self.event.key == pygame.K_LEFT :
                    self.player.actions["left"] = False
                if self.event.key == pygame.K_UP :
                    self.player.actions["up"] = False
    def update(self) :
        self.game_state_stack.peek().update()

    def draw(self) :
        self.display.blit(pygame.transform.scale(self.environment , (self.display_surface_res.x , self.display_surface_res.y)) , (0,0) )
        pygame.display.flip()
    def mainloop(self) :
        while self.running :
            self.fps = self.clock.get_fps()
            self.dt = self.clock.tick(60) / 1000
            self.get_input()
            self.update()
            self.draw()


game = Game(rect_list)

game.mainloop()
# g = Game()
