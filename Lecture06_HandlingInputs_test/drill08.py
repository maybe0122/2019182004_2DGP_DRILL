from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dirx, diry
    global right, up, move
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            move = True
            if event.key == SDLK_RIGHT:
                dirx += 1
                right = True
            elif event.key == SDLK_LEFT:
                dirx -= 1
                right = False
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_UP:
                diry += 1
                up = True
            elif event.key == SDLK_DOWN:
                diry -= 1
                up = False
        elif event.type == SDL_KEYUP:
            move = False
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            if event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1

open_canvas(TUK_WIDTH, TUK_HEIGHT)
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()
dirx, diry = 0, 0
right = True
up = True
move = False

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if move:
        if right:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif not right:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    elif not move:
        if right:
            character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
        elif not right:
            character.clip_draw(frame * 100, 100 * 2, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

    if x >= 0 and x <= TUK_WIDTH:
        x += dirx * 5
    elif x < 0 and right:
        x += dirx * 5
    elif x > TUK_WIDTH and not right:
        x += dirx * 5
    if y > 0 and y < TUK_HEIGHT:
        y += diry * 5
    elif y < 0 and up:
        y += diry * 5
    elif y > TUK_HEIGHT and not up:
        y += diry * 5

    delay(0.01)
close_canvas()
