import random

from pico2d import *

import game_world
import server

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')

        self.x = random.randint(0, server.background.w)
        self.y = random.randint(0, server.background.h)

    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom

        self.image.draw(sx, sy)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - server.background.window_left - 11, self.y - server.background.window_bottom - 11, \
               self.x - server.background.window_left + 11, self.y - server.background.window_bottom + 11
