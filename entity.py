import pygame
class Platform(pygame.sprite.Sprite) :
    """Base Class For Platforms"""
    def __init__(self , x , y , w , h , color):
        super().__init__()
        self.name = "Platform"
        self.width = w ; self.height = h
        self.color = color

        self.rect = pygame.Rect((x,y),(w,h))
        self.rect.update(x , y , w , h )




class Entity(pygame.sprite.Sprite) :
    """ Base Entity Class for Players """
    def __init__(self , color):
        super().__init__()
        vec = pygame.Vector2
        self.color = color
        self.px , self.py = 0 , 0
        self.name = str()
        self.other_player_name = str()
        self.actions = {"right" : False , "left" : False , "up" : False}
        self.other_player = pygame.sprite.Sprite()

        self.collidelist = pygame.sprite.Group()

        self.move_right_key = pygame.K_RIGHT
        self.move_left_key  = pygame.K_LEFT
        self.jump_key = pygame.K_SPACE

        self.rect = pygame.Rect((0,0) , ( 30,30 ))
        self.rect.x = 226
        self.rect.y = 470
        self.hitx , self.hity = list() , list()

        self.position = vec(500,500)
        self.delpos = vec(0,0)
        self.velocity = vec(0,0)
        self.acceleration = vec(0,0)
        self.do_gravity = True
        self.max_acceleration = 4
        self.mul = 0

    def get_input(self) :

        self.acceleration.x , self.acceleration.y =  0 , 0
        if self.actions["right"] :
            self.acceleration.x += 0.2 * 5**1
        if self.actions["left"] :
            self.acceleration.x -= 0.2 * 5**1
        if self.actions["up"] and self.velocity.y == 0 :
            self.velocity.y -= 10

    def horizontal_movement(self,dt) :
        # TODO : Add TRUE FRAMERATE INDEPENDENCE
        self.mul = (1/dt)/60
        self.acceleration.x += self.velocity.x * -.30
        self.velocity.x += self.acceleration.x * self.mul
        self.delpos.x = self.velocity.x *self.mul + ((self.acceleration.x *0.5) * (self.mul * self.mul))
        self.px = self.rect.x + self.delpos.x
        self.rect.x = round(self.px)
        hitx = pygame.sprite.spritecollide(self,self.collidelist, False)
        if hitx :
            if hitx[0].name == self.other_player_name :
                hitx[0].rect.move_ip(self.delpos.x , 0)
            if self.delpos.x > 0 :
                self.rect.right = hitx[0].rect.left
            if self.delpos.x < 0 :
                self.rect.left = hitx[0].rect.right

    def vertical_movement(self,dt) :
        self.acceleration.y = 0.4
        self.velocity.y += self.acceleration.y
        self.delpos.y = self.velocity.y + (0.5 * self.acceleration.y)
        self.rect.y += self.delpos.y
        hity = pygame.sprite.spritecollide(self, self.collidelist, False)
        if hity :
            if self.delpos.y > 0 :
                self.velocity.y = 0
                self.rect.bottom = hity[0].rect.top
            if self.delpos.y < 0 :
                self.velocity.y *= -0.1
                self.rect.top = hity[0].rect.bottom
    def move(self,dt) :
        """ Do Some Movement ^_^  """
        self.get_input()
        self.horizontal_movement(dt)
        self.vertical_movement(dt)
