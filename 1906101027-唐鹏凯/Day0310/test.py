class Student():
    def __init__(self,name,age,cn_score,ma_score,eng_score):
        self.name=name
        self.age=age
        self.cn_score=cn_score
        self.ma_score=ma_score
        self.eng_score=eng_score
    def get_name(self):
        print("姓名:",self.name)
    def get_age(self):
        print("年龄:",self.age)
    def get_course(self):
        if type(self.cn_score) != int and type(self.ma_score) != int and type(self.eng_score) != int:
            print("错误的输入")
        else:
            print("语外数成绩:",self.cn_score,self.eng_score,self.ma_score)
l = Student("唐鹏凯","20",100,100,100)
l.get_name()
l.get_age()
l.get_course()





import random
class Person():
    def __init__(self,name):
        self.name = name
        self.score=0
    
    def fingerPlay(self):
        game = ["石头","剪刀","布"]
        index = random.randint(0,2)
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
            if a_out == b_out:
                print("双方平局，出的是{}".format(a_out))
            elif (a_out=="石头" and b_out=="剪刀") or (a_out=="布"and b_out=="石头") or (a_out=="剪刀" and b_out=="布"):
                self.a.score+=1
                print("{}获得了胜利，出的是{},{}出的是{}".format(self.a.name,a_out,self.b.name,b_out))
            else:
                self.b.score+=1
                print("{}获得了胜利，出的是{},{}出的是{}".format(self.b.name,b_out,self.a.name,a_out))
        if self.a.score>self.b.score:
            print("恭喜{}获得游戏胜利,得分{}".format(self.a.name,self.b.score))
        elif self.a.score<self.b.score:
            print("恭喜{}获得游戏胜利，得分{}".format(self.b.name,self.b.score))
        else:
            print("双方平局，不分胜负")
c=Game(10000,"mark","mike")
c.playGame()