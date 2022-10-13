import play_state
import pico2d
import title_state

start_state = [title_state, play_state]
pico2d.open_canvas()


for state in start_state:
    state.enter()  # initialize
    # game loop
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
    state.exit()   # exit

pico2d.close_canvas()