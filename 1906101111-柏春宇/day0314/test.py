import random as rn             
class Sprite:
    def __init__(self,name):
        self.blood = 100         
        self.power = 12           
        self.name = name
    def attack(self, monster):
        minus = rn.randrange(self.power - 5, self.power + 5)
        print(minus)
        if monster.has_living():
            monster.minus_blood(minus)
        print(monster.name + ' 剩余血量:\n' + str(monster.blood)+ "\n")
    def minus_blood(self,num):
        self.blood -= num
    def has_living(self):         
        if self.blood > 0:
            return True
        return False
m = Sprite('人物1')
h = Sprite('人物2')
print(m.name + ' 的初始血量：100')
print(h.name + ' 的初始血量：100')
while m.has_living() and h.has_living():
    print(m.name + ' 对 ' + h.name + ' 造成伤害:' )
    m.attack(h)
    print(h.name + ' 对 ' + m.name + ' 造成伤害:')
    h.attack(m)
if m.has_living():
    print(m.name + ' 胜利!')
elif h.has_living():
    print(h.name + ' 胜利~!')
else:
    print(m.name + ' 和 ' + h.name + '均阵亡!')
