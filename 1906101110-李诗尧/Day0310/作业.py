import random
class Character():
    def __init__(self,name,blood,attact,baoji,dodge):
        self.name=name
        self.blood=blood
        self.attact=attact
        self.baoji=baoji
        self.dodge=dodge
    def role(self):
       print('名称:{},血量:{},攻击力:{},暴击率:{},闪避率:{}'.format(self.name,self.blood,self.attact,self.baoji,self.dodge))



class Game():
    def __init__(self):
        self.character1=Character('kai',100,25,0.5,0.6)
        self.character2=Character('lvbu',100,20,0.3,0.4)
    def playGame(self):
        print('游戏开始')
        count=0
        while self.character1.blood>0 and self.character2.blood>0:
            count+=1
            if random.random()<=self.character1.baoji:
                if random.random()<=self.character2.dodge:
                    self.character2.blood-=0
                else:
                    self.character2.blood-=self.character1.attact*2
            else:
                if random.random()<=self.character2.dodge:
                    self.character2.blood-=0
                else:
                    self.character2.blood-=self.character1.attact
            if random.random()<=self.character2.baoji:
                if random.random()<=self.character1.dodge:
                    self.character1.blood-=0
                else:
                    self.character1.blood-=self.character2.attact*2
            else:
                if random.random()<=self.character1.dodge:
                    self.character2.blood-=0
                else:
                    self.character1.blood-=self.character2.attact

            print('第{}轮攻击'.format(count))
            print('{}剩余血量{}:'.format(self.character1.name,self.character1.blood))
            print('{}剩余血量{}:'.format(self.character2.name,self.character2.blood))
        if self.character1.blood==0:
            print('在第{}轮，{}获胜'.format(count,self.character1))
        else:
            print('在第{}轮，{}获胜'.format(count,self.character2))
a=Character('kai',100,25,0.5,0.6)
b=Character('lvbu',100,20,0.3,0.4)
a.role()
b.role()
c=Game()
c.playGame()