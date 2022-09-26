from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('dd.png')

def line1(x, y):
    while(x < 3):
        clear_canvas()
        character.clip_draw(75 * x, y, 75, 65, 400, 130, 200, 200)
        grass.draw(400, 30)
        update_canvas()
        delay(0.051)
        x += 1

def line2(x):
    while (x < 2):
        clear_canvas()
        character.clip_draw(75 * x, 0, 75, 65, 400, 130, 200, 200)
        grass.draw(400, 30)
        update_canvas()
        delay(0.05)
        x += 1

for i in range(100):
    line1(0, 130)
    line1(0, 65)
    line2(0)

close_canvas()