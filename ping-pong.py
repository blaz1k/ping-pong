
from pygame import *
font.init()
font2= font.SysFont("Arial", 36)
main_win = display.set_mode((700,500))
display.set_caption('боевик епересете')
clock= time.Clock()
FPS= 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, w, h):
        super().__init__()
        self.image= transform.scale(image.load(player_image), (w, h))
        self.speed= speed
        self.rect= self.image.get_rect()
        self.rect.x= x
        self.rect.y= y
    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys_pressed= key.get_pressed()
        if keys_pressed[K_w] and self.rect.y<620:
            self.rect.y+= self.speed
        if keys_pressed[K_s] and self.rect.y>0:
            self.rect.y-= self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed= key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y<600:
            self.rect.y-= self.speed
        if keys_pressed[K_DOWN] and self.rect.y>0:
            self.rect.y+= self.speed


left_pl= Player2("stick.png", 50, 50, 10 ,10, 100)
background= transform.scale(image.load('bg.jpg'),(700,500))
finish= True
game = True
while game!= False:
    for e in event.get():
        if e.type == QUIT:
            game= False
    if finish == True:
        main_win.blit(background, (0, 0))
        left_pl.reset()
        left_pl.update()
    display.update()
    clock.tick(FPS)