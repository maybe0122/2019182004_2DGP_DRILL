from pico2d import *

class IDLE:
    @staticmethod
    def enter(self, event):
        print('Enter IDLE')
        self.timer = 1000
        self.dir = 0

    @staticmethod
    def exit(self):
        print('Exit IDLE')

    @staticmethod
    def do(self):
        # self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)

    @staticmethod
    def draw(self):
        # 캐릭터 애니메이션이 idle일 때 한 프레임만 그리게 수정
        if self.face_dir == 1:
            # self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
            self.image.clip_draw(0, 300, 100, 100, self.x, self.y)
        else:
            # self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
            self.image.clip_draw(0, 200, 100, 100, self.x, self.y)


class RUN:
    def enter(self, event):
        print('Enter RUN')
        if event == RD:
            self.dir += 1
        elif event == LU:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1

    def exit(self):
        print('Exit RUN')
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        # 화면 밖에 나가지 않게 범위 설정
        self.x = clamp(20, self.x, 775)

    def draw(self):
        print('Draw RUN')
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

class Boy:
    def __init__(self):
        self.x, self.y = 800//2, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.timer = 100

        self.event_que = []
        # 초기 상태
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()    # 이벤트 확인
            self.cur_state.exit(self)       # 원래 상태 나가기
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

class SLEEP:
    def enter(self, event):
        print('Enter SLEEP')
        self.frame = 0

    def exit(self):
        print('Exit SLEEP')
        pass

    def do(self):
        # sleep상태에서 애니메이션이 없게 한 프레임만 고정적으로 그리게 수정
        # self.frame = (self.frame + 1) % 8
        self.frame = 0

    def draw(self):
        print('Draw SLEEP')
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592 / 2, '', self.x - 25, self.y - 25, 100, 100)

class AUTO_RUN:
    def enter(self, event):
        print('Enter AUTO_RUN')
        if self.face_dir == 1:
            self.dir = 1
        elif self.face_dir == -1:
            self.dir = -1


    def exit(self):
        print('Exit AUTO_RUN')
        self.face_dir = self.dir
        self.dir = 0

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        # 화면 밖에 나가지 않게 범위 설정
        self.x = clamp(20, self.x, 775)
        if self.x == 20:
            self.face_dir = 1
            self.dir = 1
        if self.x == 775:
            self.face_dir = -1
            self.dir = -1

    def draw(self):
        print('Draw AUTO_RUN')
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

RD, LD, RU, LU, TIMER, AD = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_a): AD
}

next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AD: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE, AD: AUTO_RUN},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, AD: AUTO_RUN},
    AUTO_RUN: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, AD: IDLE}
}






