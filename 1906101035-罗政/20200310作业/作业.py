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
11