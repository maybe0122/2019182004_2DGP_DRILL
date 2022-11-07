from pico2d import *
import random

import game_framework
import game_world

# bird Fly Speed
PIXEL_PER_METER = (182.0 / 5)   # 182 pixel 5m
FLY_SPEED_KMPH = 30.0 # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)


# bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100, 1500), 400
        self.frame = 0
        self.dir = 1
        self.y_frame = 2
        self.image = load_image('bird_animation.png')

    def update(self):
        if self.y_frame > 0:
            self.frame = (self.frame + FRAMES_PER_ACTION * game_framework.frame_time) % 5
            if int(self.frame) == 4:
                self.y_frame -= 1
        else:
            self.frame = (self.frame + FRAMES_PER_ACTION * game_framework.frame_time) % 4
            if int(self.frame) == 3:
                self.y_frame = 2

        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time
        self.x = clamp(25, self.x, 1600 - 25)

        if self.x <= 25:
            self.dir = 1
        elif self.x >= 1600 - 25:
            self.dir = -1

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(int(self.frame)*182, 167 * self.y_frame, 182, 167, 0, 'h', self.x, self.y, 182, 167)
        elif self.dir == 1:
            self.image.clip_draw(int(self.frame)*182, 167 * self.y_frame, 182, 167, self.x, self.y)
