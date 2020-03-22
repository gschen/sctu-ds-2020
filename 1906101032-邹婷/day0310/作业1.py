import random
class Person():
    def __init__(self,name,xueliang,gongjili,baojilv,shanbilv):
        self.name=name
        self.xueliang=xueliang
        self.gongjili=gongjili
        self.baojilv=baojilv
        self.shanbilv=shanbilv
    def role(self):
        print('玩家名称:%s\n血量:%s\n攻击力:%s\n暴击率:%s\n闪避率:%s'%(self.name,self.xueliang,self.gongjili,self.baojilv,self.shanbilv))
a=Person('A家',500,500,0.2,0.4)
b=Person('B家',600,600,0.3,0.6)
a.role()
b.role()
class Game():
    def __init__(self):
        self.person1=a
        self.person2=b
    def playGame(self):
        print('游戏开始')
        count=0
        while self.person1.xueliang>0 and self.person2.xueliang>0:
            count+=1
            if random.random()<=self.person1.baojilv:
                if random.random()<=self.person2.shanbilv:
                    self.person2.xueliang-=0
                else:
                    self.person2.xueliang-=self.person1.gongjili*2
            else:
                if random.random()<=self.person2.shanbilv:
                    self.person2.xueliang-=0
                else:
                    self.person2.xueliang-=self.person1.gongjili
            if random.random()<=self.person2.baojilv:
                if random.random()<=self.person1.shanbilv:
                    self.person1.xueliang-=0
                else:
                    self.person1.xueliang-=self.person2.gongjili*2
            else:
                if random.random()<=self.person1.shanbilv:
                    self.person2.xueliang-=0
                else:
                    self.person1.xueliang-=self.person2.gongjili
            if self.person1.xueliang<=0:
                self.person1.xueliang=0
            if self.person2.xueliang<=0:
                self.person2.xueliang=0
            print('第%d攻击:'%count)
            print('A家:剩余血量:%d'%self.person1.xueliang)
            print('B家:剩余血量:%d'%self.person2.xueliang)
        if self.person1.xueliang==0:
            print('经过%d轮攻击,A家胜利.'%count)
        else:
            print('经过%d轮攻击,B家胜利.'%count)
a=Person('A家',500,500,0.2,0.4)
b=Person('B家',600,600,0.3,0.6)
c=Game()
c.playGame()



                
