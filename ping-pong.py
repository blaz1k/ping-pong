
from pygame import *
font.init()
font1= font.SysFont("Arial", 72)
font2= font.SysFont("Arial", 36)
main_win = display.set_mode((700,500))
display.set_caption('боевик епересете')
clock= time.Clock()
FPS= 120

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

class Player(GameSprite):
    def update0(self):
        keys_pressed= key.get_pressed()
        if keys_pressed[K_s] and self.rect.y<400:
            self.rect.y+= self.speed
        if keys_pressed[K_w] and self.rect.y>0:
            self.rect.y-= self.speed
    def update1(self):
        keys_pressed= key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y<400:
            self.rect.y+= self.speed
        if keys_pressed[K_UP] and self.rect.y>0:
            self.rect.y-= self.speed

speed_x = 3
speed_y =3

win_right_label= font1.render("победа правого",True, (0, 0 ,255))
win_left_label= font1.render("победа левого", True, (255, 0 ,0))
ball= GameSprite("snowball.png", 50, 50, 3, 50, 50)
left_pl= Player("shield_r.png", 0, 50, 10 ,50, 100)
right_pl= Player("shield.png", 650, 50, 10 ,50, 100)
background= transform.scale(image.load('background.png'),(700,500))
finish= True
game = True
while game!= False:
    for e in event.get():
        if e.type == QUIT:
            game= False
    if finish == True:
        main_win.blit(background, (0, 0))
        left_pl.reset()
        left_pl.update0()
        ball.reset()
        right_pl.reset()
        right_pl.update1()
        ball.rect.y += speed_y
        ball.rect.x += speed_x
        if ball.rect.y< 0 or ball.rect.y> 450:
            speed_y *= -1
        if sprite.collide_rect(ball, right_pl) or sprite.collide_rect(ball, left_pl):
            speed_x *= -1
        
        if ball.rect.x <-50:
            main_win.blit(win_right_label, (150, 250))
            finish = False
        if ball.rect.x >750:
            main_win.blit(win_left_label, (150, 200))
            finish = False
    display.update()
    clock.tick(FPS)
    