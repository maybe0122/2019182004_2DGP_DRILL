import random

from pico2d import *

import game_world
import server
from background import FixedBackground as bg

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')

        self.x = random.randint(0, 1837)
        self.y = random.randint(0, 1109)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 11, self.y - 11, self.x + 11, self.y + 11