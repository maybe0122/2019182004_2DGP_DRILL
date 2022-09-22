from pico2d import *
import math

def square():
    for x in range(20, 780):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x += 2
        delay(0.01)
    for y in range(90, 560):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.01)
    for x in range(780, 20, -1):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        delay(0.01)
    for y in range(560, 90, -1):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.01)
    for x in range(20, 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x += 2
        delay(0.01)

def circle():
    x = 600
    y = 390
    r = 250
    for angle in range(0, 180):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x + r * math.cos(math.radians(angle)), y + r *math.sin(math.radians(angle)))
    for angle in range(0, 180):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x - r * math.cos(math.radians(angle)), y - r *math.sin(math.radians(angle)))




open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


command = False

while True:
        if(command):
            squared()
            command = True
        else:
            circle()
            command = False


close_canvas()
