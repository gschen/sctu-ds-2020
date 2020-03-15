#猜拳游戏

import random
class Person():
    def __init__(self,name):
        self.name=name
        self.score=0
    def fingerPlay(self):
        game=["布","剪刀","石头"]
        index=random.randint(0,2)
        #random.choice(geme)
        return game[index]
class Game():
    def __init__(self,number,aname,bname):
        self.number=number
        self.a=Person(aname)
        self.b=Person(bname)
    def playGame(self):
        for i in range(self.number):
            a_out=self.a.fingerPlay()
            b_out=self.b.fingerPlay()
            print()
            if a_out==b_out:
                print("双方平局，出的是%s" % (a_out))
            elif (a_out=="石头" and b_out=="剪刀") or (a_out=="布" and b_out=="石头") or (a_out=="剪刀" and b_out=="布"):
                print("%s获得胜利,出的是%s,%s出的是%s" % (self.a.name,a_out,self.b.name,b_out))
                self.a.score+=1
            else:
                self.b.score+=1
                print("%s获得胜利,出的是%s,%s出的是%s" % (self.b.name,b_out,self.a.name,a_out))
        if self.a.score>self.b.score:
            print("恭喜%s获得游戏胜利,得分%d" % (self.a.name,self.a.score))
        elif self.a.score<self.b.score:
            print("恭喜%s获得游戏胜利,得分%d" % (self.b.name,self.b.score))
        else:
            print("双方平局，不分胜负")
one=Game(600,"林以信","林以北")
one.playGame()