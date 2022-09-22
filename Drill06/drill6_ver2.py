from pico2d import *
import math

def square():
    for x in range(400, 780):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x += 2
        delay(0.001)
    for y in range(90, 560):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.001)
    for x in range(780, 20, -1):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        delay(0.001)
    for y in range(560, 90, -1):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.001)
    for x in range(20, 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x += 2
        delay(0.001)

def circle():
    x = 400
    y = 350
    r = 260
    for angle in range(-90, 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x + r * math.cos(math.radians(angle)), y + r *math.sin(math.radians(angle)))
        delay(0.01)
    for angle in range(-90, 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x - r * math.cos(math.radians(angle)), y - r *math.sin(math.radians(angle)))
        delay(0.01)

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


command = True

while True:
        if(command):
            pass
            square()
            command = False
        else:
            circle()
            command = True


close_canvas()
