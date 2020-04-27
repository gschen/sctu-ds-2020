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

    def setRank(self, Rank):
        self.Rank = Rank

    def getHp(self):
        return self.Hp

    def setHp(self, Hp):
        self.Hp = Hp

    def normal_kill(self):
        time.sleep(0.5)
        return -(self.Angry * self.Rank)

    def random_defend(self):
        temp = random.randint(-10, self.Defend)  # Defend越大则防御能力越大
        if temp > 0:
            return True

    def outputinfo(self):
        print('名称：', self.__Name, 'Hp：', self.Hp, '等级：', self.Rank, '技能冷却：', self.Bubble)


class Tank(Player):
    def __init__(self, Name, Angry, Hp, Rank, Bubble, Defend, recovery):
        threading.Thread.__init__(self)
        Player.__init__(self, Name, Angry, Hp, Rank, Bubble, Defend)
        self.__recovery = recovery

    def random_defend(self):
        temp = random.randint(-10, self.Defend + self.__recovery)
        if temp > 0:
            return True

    def regenerate(self):
        if self.Bubble > 0:
            time.sleep(0.5)
            if self.Hp < 100:
                self.Hp += 30
                if self.Hp > 100:
                    self.Hp = 100
            self.Bubble -= 10
        else:
            time.sleep(2)
            self.Hp += 5


class Assassin(Player):
    def __init__(self, Name, Angry, Hp, Rank, Bubble, Defend, Raid):
        Player.__init__(self, Name, Angry, Hp, Rank, Bubble, Defend)
        self.__Raid = Raid

    def Surprise_Attack(self):
        time.sleep(0.5)
        temp = 0 - self.Angry * self.Rank
        if self.Bubble > 0:
            temp2 = random.randint(-10, 20)
            if temp2 > 0:
                temp -= self.__Raid
                self.Bubble -= 10
        return temp


class Archmage(Player):
    def __init__(self, Name, Angry, Hp, Rank, Bubble, Defend, Magic):
        threading.Thread.__init__(self)
        Player.__init__(self, Name, Angry, Hp, Rank, Bubble, Defend)
        self.__Magic = Magic

    def magicHp(self):
        if self.Bubble > 0:
            temp = random.randint(50, 100)
            if temp > self.__Hp:
                self.__Hp = temp + self.__Magic
            self.Bubble -= 10

    def magic_kill(self):
        temp = 0
        if self.Bubble > 0:
            temp2 = random.randint(-10, 20)
            if temp2 > 0:
             temp -= self.__Magic
             self.Bubble -= 10
        return temp


def run_tank(tank, assassin):
    while tank.getHp() > 0 and assassin.getHp() >= 0:
        assassin.setHp(assassin.getHp() + tank.normal_kill())
        tank.outputinfo()
        time.sleep(0.2)
        tank.regenerate()
    if tank1.getHp() > 0:
        print("派大星赢了")
    else:
        print("海绵宝宝赢了")


def run_assassin(tank, assassin):
    while assassin.getHp() > 0 and tank.getHp() >= 0:
        if tank.random_defend() is True:
            tank.setHp(tank.getHp() + assassin.normal_kill())
        else:
            assassin.Surprise_Attack()
        assassin.outputinfo()
        time.sleep(0.2)



if __name__ == '__main__':
    print("-------------- 一刀999！--------------\n")
    time.sleep(1)
    print("所有角色有普通杀与普通防御功能，Hp代表血量，Bubble代表技能冷却时间\n")
    time.sleep(1)
    print("有坦克、刺客、法师三个角色\n")
    time.sleep(1)
    print("坦克 Tank\n")
    print("坦克特殊技能能够迅速恢复失掉的血量\n")
    time.sleep(1)
    print("刺客 Assassin\n")
    print("刺客身手矫健\n")
    time.sleep(1)
    print("法师 Archmage\n")
    print("法师拥有魔法\n")
    time.sleep(1)
    print("游戏start----------------------------------------------------！")
    time.sleep(1)
    # Name, Angry, Hp, Rank, Bubble, Defend, Magic):
    tank1 = Tank("派大星", 5, 100, 1, 100, 20, 5)
    assassin1 = Assassin("海绵宝宝", 5, 100, 1, 100, 20, 10)
    # run_tank(tank1, assassin1)
    # run_assassin(tank1, assassin1)
    

    threads = []
    t1 = threading.Thread(target=run_tank, args=(tank1, assassin1))
    threads.append(t1)
    t2 = threading.Thread(target=run_assassin, args=(tank1, assassin1))
    threads.append(t2)
    for t in threads:
        # t.setDaemon(True)
        t.start()