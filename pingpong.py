
from pygame import *
from random import randint

FPS = 60
clock = time.Clock()
font.init()
font = font.SysFont('Arial', 35)
window_width = 700
window_height = 500
window = display.set_mode((window_width, window_height))
display.set_caption("ping-pong")

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,playerX,playerY,playerspeedX,playerspeedY,x_size,y_size):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(x_size,y_size))
        self.rect = self.image.get_rect()
        self.speedX = playerspeedX
        self.speedY = playerspeedY
        self.rect.x = playerX
        self.rect.y = playerY
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y< 400:
            self.rect.y+=self.speedY
        if keys[K_w] and self.rect.y> 0:
            self.rect.y-=self.speedY
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y< 400:
            self.rect.y+=self.speedY
        if keys[K_UP] and self.rect.y> 0:
            self.rect.y-=self.speedY

class Ball(GameSprite):
    def update(self):
        pass

player_1 = Player('racket.png',0,240,5,5,50,150)
player_2 = Player('racket.png',650,240,5,5,50,150)
ball = Ball('tenis_ball.png',325,250,4,4,63,63)

game = True
finish = False
while game:
    import time
    for e in event.get():
        if e.type == QUIT:
            game = False
        else:
            pass
    if finish != True:
        window.fill((127,199,255))
        ball.rect.x += ball.speedX
        ball.rect.y += ball.speedY
        if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
            ball.speedX *= -1
        if ball.rect.y <= 0 or ball.rect.y >= 450:
            ball.speedY *= -1
        if ball.rect.x <= 0:
            player_1_lost = font.render('Player 1 lost',True,(0,0,0))
            window.blit(player_1_lost,(280,240))
            finish = True
        if ball.rect.x >= 650:
            player_2_lost = font.render('Player 2 lost',True,(0,0,0))
            window.blit(player_2_lost,(280,240))
            finish = True
        player_1.update_1()
        player_1.reset()
        player_2.update_2()
        player_2.reset()
        ball.update()
        ball.reset()
    display.update()
    clock.tick(FPS)
