from pico2d import *
import game_framework
import play_state

image = None

def enter():
    global image
    image = load_image('add_delete_boy.png')

def exit():
    global image
    del image

def update():
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_EQUALS:          # 키보드에 =과 +이 같이 있어서 등호로 입력받게함
                    play_state.boys.append(play_state.Boy())
                    play_state.count += 1
                    game_framework.pop_state()
                case pico2d.SDLK_MINUS:
                    if(play_state.count > 1):
                        play_state.boys.pop()
                        play_state.count -= 1
                    game_framework.pop_state()
