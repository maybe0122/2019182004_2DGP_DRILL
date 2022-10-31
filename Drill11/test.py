# class Star:
#     name = 'Star'   # class 변수
#     x = 100         # class 변수
#
#     def change():
#         x = 200
#         print('x is ', x)
#
# print('x is ', Star.x)
# Star.change()
# print('x is ', Star.x)
#
# star = Star()   # 생성자가 없는데 생성이 된다? O / 객체는 생성은 됨
# print(star.x)   # 비록 객체의 변수로 액세스했으나, 같은 이름의 클래스 변수가 우선됨
# # 오류 코드 => star.change()    # 실행 x Star.chang(star)와 동일

# class Player:
#     type = 'Player'
#
#     def __init__(self): # 생성자
#         self.x = 100
#
#     def where(self):
#         print(self.x)
#
# player = Player()
# player.where()
#
# print(Player.type)
#
# # 오류 코드 Player.where()
# Player.where(player)    # player.where() 과 같음

table = { "SLEEP": {"HIT":"WAKE"}, "WAKE": {"TIMER10":"SLEEP"} }