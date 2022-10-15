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
    def __init__(self , rect_list:list) :
        self.environment_surface_res = Res(1280,720)
        self.display_surface_res = Res(1408 , 736)
        self.rect_list = rect_list

        self.trash = "Hi "

        self.player1 = Entity("blue")
        self.player1.name = "Player1"

        self.player2 = Entity("red")
        self.player2.name = "Player2"
        self.player2.jump_key = pygame.K_UP


        self.all_objects =pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()


        self.players.add(self.player1 , self.player2)


        for i in self.rect_list :
            self.platforms.add(Platform(i.x , i.y  , i.w , i.h ,"black"))

        self.player1.collidelist.add(*self.platforms.sprites())
        self.player2.collidelist.add(*self.platforms.sprites())
        self.all_objects.add(*self.platforms.sprites() ,self.player1 , self.player2)

        self.running = True
    def update(self) :
        self.player1.move(1)
        self.player2.move(1)

    def mainloop(self) :
        while self.running :
            self.update()
            # print(self.player1.actions , self.player2.actions , sep='____' * 10 )
            print(self.trash)


if __name__ == '__main__':
    game = Game(rect_list)

    game.mainloop()
