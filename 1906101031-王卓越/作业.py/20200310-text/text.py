import random
class Arctor:
    def __init__(self,n):
        self.name=n[0]
        self.blood=n[1]
        self.attack=n[2]
        self.violence=n[3]
        self.DOD=n[4]
class Game:
    def __init__(self,a,b):
        self.num=0
        self.a=Arctor(a)
        self.b=Arctor(b)
    def violence(self,n):
        if random.random()<=n.violence:
            self.s=n.attack*2
        else:
            self.s = n.attack
        return self.s
    def DOD(self,n):
        if random.random()<=n.DOD:
            return True
        else:
            return False
    def playGame(self):
        while self.a.blood>0 and self.b.blood>0:
            self.violence(self.b)
            if self.DOD(self.a):
                self.a.blood-=0
            else:
                self.a.blood-=self.s
            self.violence(self.a)
            if self.DOD(self.b):
                self.b.blood-=0
            else:
                self.b.blood-=self.s
            self.num+=1
            if self.a.blood<=0:
                print('最终{}胜利，血量还剩{},{}失败血量{}'.format(self.b.name,self.b.blood,self.a.name,self.a.blood))
                break
            if self.b.blood<=0:
                print('最终{}胜利,血量还剩{},{}失败血量{}'.format(self.a.name,self.a.blood,self.b.name,self.b.blood))
                break
            print('这是第{}轮游戏，{}的血量还剩{}，{}的血量还剩{}'.format(self.num,self.a.name,self.a.blood,self.b.name,self.b.blood))
f=Game(('张三',80,5,0.3,0.2),('李四',90,6,0.2,0.2))
f.playGame()


