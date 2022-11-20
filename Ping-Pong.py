from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,width,height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-120:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-120:
            self.rect.y += self.speed

win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill((255,255,255))
FPS = 60
clock = time.Clock()
racket1 = Player("racket.png",30,200,4,50,125)
racket2 = Player("racket.png",520,200,4,50,125)

game = True
while game  == True:
    for e in event.get():
        if e .type == QUIT:
            game == False
    window.fill((255,255,255))
    racket1.update_l()
    racket2.update_r()
    racket1.reset()
    racket2.reset()

    display.update()
    clock.tick(FPS)
