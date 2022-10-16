import pico2d
import play_state
import logo_state
import game_framework
states = [logo_state]    # 모듈을 변수로 저장

pico2d.open_canvas()
# for state in states:
#     state.enter()   # 초기화
#     # game loop
#     while state.running:
#         state.handle_events()
#         state.update()
#         state.draw()
#     state.exit()  # 종료

for state in states:
    game_framework.run(state)

pico2d.close_canvas()