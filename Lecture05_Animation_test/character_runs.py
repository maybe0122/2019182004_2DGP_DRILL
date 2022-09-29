from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

x = 0
frame = 0
while (x < 800):
    clear_canvas()

    # pico2d는 왼쪽 밑에가 원점, clip에서 left, bottom 이 자를 그림의 좌표, width, height 가 자를 범위
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    grass.draw(400, 30)
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    delay(0.05)
    get_events()

close_canvas()
