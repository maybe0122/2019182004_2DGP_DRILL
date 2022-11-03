from pico2d import *

class Grass:
    image = None
    def __init__(self):
        self.x, self.y = 400, 30
        if Grass.image == None:
            self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass
