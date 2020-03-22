import random
class Chrac():
    def __init__ (self,name):
        self.name = name
        self.blood = 100
        self.attack = 5
        self.crit = 0.2
        self.dodge = 5
        
class Game():
    def __init__(self,p1,p2):
        self.a = Chrac(p1)
        self.b = Chrac(p2)
    def round(self):
        sum = 0
        while self.a.blood > 0 and self.b.blood > 0:
            sum+=1
            print("第{}几回合".format(sum))
            if random.randint(1,10) < self.a.dodge:
                print("{}躲避了来自{}的伤害".format(self.a.name,self.b.name))
            else:
                if self.a.crit >= random.random():
                    self.b.blood -= self.a.attack*2
                    print("{}对{}打出了暴击伤害".format(self.a.name,self.b.name))
                else:         
                    self.b.blood -= self.a.attack
                    print("{}打中了{}".format(self.a.name,self.b.name))

            if self.b.dodge > random.randint(1,10):
                print("{}躲避了来自{}的伤害".format(self.b.name,self.a.name))
            else:
                if self.b.crit >= random.random():
                    self.a.blood -= self.b.attack*2
                    print("{}对{}打出了暴击伤害".format(self.b.name,self.a.name))
                else:         
                    self.a.blood -= self.b.attack
                    print("{}打中了{}".format(self.b.name,self.a.name))
            print("{}还剩{}血量".format(self.a.name,self.a.blood))
            print("{}还剩{}血量".format(self.b.name,self.b.blood))
            print("--------------------------------------------")
            
            if self.a.blood <= 0 :
                
                print("{}赢了".format(self.b.name))
                break
            elif self.b.blood <= 0 :
                
                print("{}赢了".format(self.a.name))
                break
            elif self.a.blood <=0 and self.b.blood <=0:
                print("同归于尽")
                break
            


            
x,y = map(str,input().split())
s = Game(x,y)
s.round()



