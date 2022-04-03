from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img, spd=10, x=400, y=200, w=50, h=50):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.spd = spd
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        win.blit(self.image ,(self.rect.x, self.rect.y))

class Racket(GameSprite):
    def move1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.spd
        if keys_pressed[K_DOWN] and self.rect.y < win_height-125:
            self.rect.y += self.spd
    def move2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.spd
        if keys_pressed[K_s] and self.rect.y < win_height-125:
            self.rect.y += self.spd

class Ball(GameSprite):
    def move(self):
        pass
            
win_width = 800
win_height = 400

win = display.set_mode((win_width, win_height))
display.set_caption('PingPong')

win.fill((200,255,255))

mixer.init()
mixer.music.load('music.ogg')
mixer.music.play()
hit_sound = mixer.Sound('sound.ogg')

#спрайты
ball = Ball ('ball.png', 10, 400, 200, 50, 50)
racket2 = Racket('racket.png', 10, 25, 140, 25, 125)
racket1 = Racket('racket.png', 10, 750, 140, 25, 125)

#переменные
FPS = 60
clock = time.Clock()
game = True
stop = False

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    win.fill((200,255,255))
    ball.draw()
    racket1.draw()
    racket1.move1()
    racket2.draw()
    racket2.move2()

    display.update()
    clock.tick(FPS)