"""
import random
import threading
import time


class Player(threading.Thread):
    def __init__(self, Name, Angry, Hp, Rank, Bubble, Defend):
        threading.Thread.__init__(self)
        self.__Name = Name
        self.Angry = Angry
        self.Hp = Hp
        self.Rank = Rank
        self.Bubble = Bubble
        self.Defend = Defend

    def getRank(self):
        return self.Rank

    def getHp(self):
        return self.Hp

    def setHp(self, Hp):
        self.Hp = Hp

    def normal_kill(self):
        time.sleep(0.5)
        return -(self.Angry * self.Rank)

    def random_defend(self):
        temp = random.randint(-10, self.Defend) 
        if temp > 0:
            return True

    def outputinfo(self):
        print('名称：', self.__Name, 'Hp：', self.Hp, '等级：', self.Bubble)


class Tank(Player):
    def __init__(self, Name, Angry, Hp, Rank, Bubble, Defend, recovery):
        threading.Thread.__init__(self)
        Player.__init__(self, Name, Angry, Hp, Rank, Bubble, Defend)
        self.__recovery = recovery

    def random_defend(self):
        temp = random.randint(-10, self.Defend + self.__recovery)
        if temp > 0:
            return True
111
"""
import random
class Person():
    def __init__(self,name,blood,power,crit,avoid):
        self.name=name
        self.blood=blood
        self.power=power
        self.crit=crit
        self.avoid=avoid
def attack(self,object):
    if random.random() >=object.avoid:
        if random.random() <=self.crit:
            object.blood-=self.power*2
        else:
            object.blood-=self.power

class Game():
    def __init__(self,one,two):
        self.one=one
        self.two=two
def solo(self):
    while Ture:
       self. one.attack(two)
            if self.two.blood<=0:
            print("{}活到了最后".format(self.one))
            break
           self. two.attack(one)
            if self.one.blood<=0:
            print(print("{}活到了最后".format(self.one)))
lz=Person("lz",470,47,2,2)
xx=Person("xx",460,60,0,3)