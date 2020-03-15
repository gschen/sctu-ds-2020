import random
class Person():
    def __init__(self,name,xueliang,gongjili,baojilv,shanbilvu):
        self.name=name
        self.xueliang=xueliang
        self.gongjili=gongjili
        self.baojilv=baojilv
        self.shanbilvu=shanbilvu
    def role(self):
        print('玩家名称:%s,血量:%s,攻击力:%s,暴击率:%s,闪避率:%s'%(self.name,self.xueliang,self.gongjili,self.baojilv,self.shanbilv))
class Game():
    def __init__(self):
        self.aname=a
        self.bname=b
    def playGame(self):
        count=0
        while self.aname.xueliang>0 and self.bname.xueliang>0:
            count+=1
            if random.random()<=self.aname.baojilv:
                if random.random()<=self.bname.shanbilv:
                    self.bname.xueliang-=0
                else:
                    self.bname.xueliang-=self.aname.gongjili*2
            else:
                if random.random()<=self.bname.shanbilv:
                    self.bname.xueliang-=0
                else:
                    self.bname.xueliang-=self.aname.gongjili
            if random.random()<=self.bname.baojilv:
                if random.random()<=self.aname.shanbilv:
                    self.aname.xueliang-=0
                else:
                    self.aname.xueliang-=self.bname.gongjili*2
            else:
                if random.random()<=self.aname.shanbilv:
                    self.bname.xueliang-=0
                else:
                    self.aname.xueliang-=self.bname.gongjili
            if self.aname.xueliang<=0:
                self.aname.xueliang=0
            if self.bname.xueliang<=0:
                self.bname.xueliang=0
            print('第%d攻击:'%count)
            print('A家:剩余血量:%d'%self.aname.xueliang)
            print('B家:剩余血量:%d'%self.bname.xueliang)
        if self.aname.xueliang==0:
            print('经过%d轮攻击,A家胜利,'%count)
        else:
            print('经过%d轮攻击,B家胜利,'%count)
a=Person('A家',500,500,0.2,0.4)
b=Person('B家',600,600,0.3,0.6)
c=Game()
c.playGame()


                
