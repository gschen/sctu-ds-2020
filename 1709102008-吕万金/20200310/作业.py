import random
class Character():
    def __init__(self,name,HP,ATK,SPD,DOD):
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.SPD = SPD
        self.DOD = DOD
# class Fight(Character):
#     def __init__(self,player1,player2):
#         self.a = player1
#         self.b = player2
#     def playgame(self):
#         print('游戏开始')
#         round = 1
#         while self.a.HP > 0 and self.b.HP > 0: