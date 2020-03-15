import random
class Person():
    def __init__(self,name,HP,STR):
        self.name=name
        self.HP=HP
        self.STR=STR
      
    def fingerPlay(self):
        game=['攻击力','暴击率','闪避率']
        index=random.randint(0,2)
        return game[index]

class Game(Person):
    def __init__(self,aname,bname,HP,STR):
        self.a=Person(aname,HP,STR)
        self.b=Person(bname,HP,STR)
        self.HP=HP
        self.STR=STR
    def playGame(self):
        self.a_out=self.a.fingerPlay()
        self.b_out=self.b.fingerPlay()
        while self.a.HP>0 and self.b.HP>0:
            if self.a_out=='攻击力':
                if self.b_out=='攻击力':
                    self.a.HP=self.a.HP-self.STR
                    self.b.HP=self.b.HP-self.STR
                elif self.b_out=='闪避率':
                    self.a.HP=self.a.HP-self.STR*0
                    self.b.HP=self.b.HP-self.STR*0
                else:
                    if random.random(0,1)<=0.2:
                        self.b.HP=self.b.HP-self.STR
                        self.a.HP=self.a.HP-self.STR*2
                    else:
                        self.b.HP=self.b.HP-self.STR
                        self.a.HP=self.a.HP-self.STR*0
            elif self.a_out=='闪避率':
                if self.b_out=='攻击力':
                    self.a.HP=self.a.HP-self.STR
                    self.b.HP=self.b.HP-self.STR
                elif self.b_out=='闪避率':
                    self.a.HP=self.a.HP-self.STR*0
                    self.b.HP=self.b.HP-self.STR*0
                else:
                    if random.random(0,1)<=0.2:
                        self.b.HP=self.b.HP-self.STR*0
                        self.a.HP=self.a.HP-self.STR*0
                    else:
                        self.b.HP=self.b.HP-self.STR*0
                        self.a.HP=self.a.HP-self.STR*0
            else:
                if random.random(0,1)<=0.2:
                    if self.b_out=='攻击力':
                        self.a.HP=self.a.HP-self.STR
                        self.b.HP=self.b.HP-self.STR*2
                    elif self.b_out=='闪避率':
                        self.a.HP=self.a.HP-self.STR*0
                        self.b.HP=self.b.HP-self.STR*0
                    else:
                        if random.random(0,1)<=0.2:
                            self.b.HP=self.b.HP-self.STR*2
                            self.a.HP=self.a.HP-self.STR*2
                        else:
                            self.b.HP=self.b.HP-self.STR*2
                            self.a.HP=self.a.HP-self.STR*0
                else:
                    if self.b_out=='攻击力':
                        self.a.HP=self.a.HP-self.STR
                        self.b.HP=self.b.HP-self.STR*0
                    elif self.b_out=='闪避率':
                        self.a.HP=self.a.HP-self.STR*0
                        self.b.HP=self.b.HP-self.STR*0
                    else:
                        if random.random(0,1)<=0.2:
                            self.b.HP=self.b.HP-self.STR*0
                            self.a.HP=self.a.HP-self.STR*2
                        else:
                            self.b.HP=self.b.HP-self.STR*0
                            self.a.HP=self.a.HP-self.STR*0
            print(self.a.HP,self.b.HP)
rone=Game('A','B',10,2)
rone.playGame()