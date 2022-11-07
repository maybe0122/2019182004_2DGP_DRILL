from pico2d import *
import random

import game_framework
import game_world

# bird Fly Speed
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
FLY_SPEED_KMPH = 30.0 # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)


# bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACION = 5

class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100, 1500), 100
        self.frame = 0
        self.dir, self.face_dir = 1, 1
        self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACION * game_framework.frame_time) % 5
        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time
        self.x = clamp(25, self.x, 1600 - 25)
        if self.x <= 25:
            self.dir = 1
        elif self.x >= 1600 - 25:
            self.dir = -1

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(int(self.frame)*183, 126, 183, 126, 0, 'v', self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(int(self.frame)*183, 126 * 2, 183, 126, self.x, self.y)
