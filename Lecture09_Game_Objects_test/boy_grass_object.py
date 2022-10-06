from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self): # 생성자
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Ball:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = 400, 72

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += 7

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self): # 소년의 행위 구현.
        self.frame = random.randint(0, 7)
        self.x += 5 # 속성값을 바꿈으로써, 행위(오른쪽으로 이동)를 구현

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

ball = Ball()
team = [Boy() for i in range(11)]
grass = Grass()

runnig = True

# game main loop code
while runnig:
    handle_events() # 키 입력 받아들이는 처리

    for boy in team:
        if (boy.x <= ball.x - 20 and ball.x - 20 <= boy.x + 20):
            ball.update()
            # delay(0.05)
        boy.update() # 소년의 상호작용

    clear_canvas()
    grass.draw()
    ball.draw()
    for boy in team:
        boy.draw()


    update_canvas()

    delay(0.05)

# finalization code
close_canvas()