import random
class Person():
    def __init__(self,name,blood,fight):
        self.name=name
        self.blood=blood
        self.fight=fight
    def gongjiplay(self):
        game=['攻击力','暴击','闪避']
        index=random.randint(0,2)
        return game[index]

class Game(Person):
    def __init__(self,aname,bname,blood,fight):
        self.a=Person(aname,blood,fight)
        self.b=Person(bname,blood,fight)
        self.blood=blood
        self.fight=fight

    def playGame(self):
        for i in range(0,2):
            self.a_out=self.a.gongjiplay()
            self.b_out=self.b.gongjiplay()
            while self.a.blood >0 and self.b.blood > 0:
                if  self.a_out=='攻击力':
                    if self.b_out=='攻击力':
                        self.a.blood=self.a.blood-self.a.fight*2
                        self.b.blood=self.b.blood-self.a.fight*2
                    elif self.b_out=='闪避':
                        self.a.blood=self.a.blood-self.a.fight*0
                        self.b.blood=self.b.blood-self.b.fight*0
                    else:
                        if random.randint(0,2)<=0.2:
                            self.a.blood=self.a.blood-self.a.fight
                            self.b.blood=self.b.blood-self.b.fight*2
                        else:
                            self.a.blood=self.a.blood-self.a.fight
                            self.b.blood=self.b.blood-self.b.fight*0
                elif self.a_out=='闪避':
                    if self.b_out=='攻击力':
                        self.a.blood=self.a.blood-self.a.fight*0
                        self.b.blood=self.b.blood-self.b.fight*0
                    elif self.b_out=='闪避':
                        self.a.blood=self.a.blood-self.a.fight*0
                        self.b.blood=self.b.blood-self.b.fight*0
                    else:
                        if random.randint(0,2)<=0.2:
                            self.a.blood=self.a.blood-self.a.fight*2
                            self.b.blood=self.b.blood-self.b.fight*2
                        else:
                            self.a.blood=self.a.blood-self.a.fight*2
                            self.b.blood=self.b.blood-self.b.fight*0
                else:
                    if self.b_out=='攻击力':
                        self.a.blood=self.a.blood-self.a.fight*0
                        self.b.blood=self.b.blood-self.b.fight*2
                    elif self.b_out=='闪避':
                        self.a.blood=self.a.blood-self.a.fight*0
                        self.b.blood=self.b.blood-self.b.fight*0
                    else:
                        if random.randint(0,2)<=0.2:
                            self.a.blood=self.a.blood-self.a.fight*2
                            self.b.blood=self.b.blood-self.b.fight*0
                        else:
                            self.a.blood=self.a.blood-self.a.fight*0
                            self.b.blood=self.b.blood-self.b.fight*2
            print(self.a_out.blood,self.b_out.blood)
M=Game('张三','李四',100,5)
M.playGame()