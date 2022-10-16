import random

import pico2d
from pico2d import *
import game_framework
import title_state
import item_state
import add_state

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        location = random.randint(0, 400)
        self.x, self.y = location, 90
        self.frame = 0
        self.dir = 1    # right
        self.image = load_image('animation_sheet.png')
        self.item = None
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        if self.x > 800:
            self.x = 800
            self.dir = -1   # left
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.item == 'Ball':
            self.ball_image.draw(self.x+10, self.y+50)
        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x + 10, self.y + 50)

        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)
            elif event.key == SDLK_b:
                game_framework.push_state(add_state)


boys = []    # c로 따지믄 NULL
grass = None
running = True
count = 0

# 초기화
def enter():
    global boys, grass, running, count
    boys += [Boy()]
    count += 1
    grass = Grass()
    running = True

# finalization code
def exit():
    global boys, grass
    del boys
    del grass

def update():
    for boy in boys:
        boy.update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    grass.draw()
    for boy in boys:
        boy.draw()


def pause():
    pass

def resume():
    pass

def test_self():
    import sys
    pico2d.open_canvas()
    game_framework.run(sys.modules['__main__'])
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
