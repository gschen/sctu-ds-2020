import random
class Person():
    def __init__(self,name):
        self.name=name

    def fingerplay(self):
        game=["石头","剪刀","布"]
        index=random.randint(0,2)
        return game[index
        
Class Game():
    def __init__(self):
        self.number==number
        self.a=Person()
        self.b=Person()
    
    def playGame(self):
        for i in range(self.number):
            a_out=self.a.fingerPlay()
            b_out=self.b.fingerPlay()
            if a_out==b_out:
                print("双方出局，出的是{}".format(a_out))
            elif(a_out=="石头" and b_out=="剪刀") or (a_out=="布" and b_out=="石头") or (a_out=="剪刀" and b_out=="布"):
                print("{}获得胜利,出的是{},{}出的是{}".format(self.a.name,a_out,self.b.name,b_out))
            else:
                print("{}获得胜利,出的是{},{}出的是{}".format(self.b.name,b_out,self.a.name,a_out))

    
