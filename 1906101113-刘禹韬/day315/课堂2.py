#猜拳

import random

class Person():
    def __init__(self,name):
        self.name=name
    def fingerplay(self):
        game=['剪刀','石头','布']
        index=random.randint(0,2)
        return game[index]

class Game():
    def __init__(self,number,aname,bname):
        self.number=number
        self.a=Person(aname)
        self.b=Person(bname)
    def playGame(self,acount=0,bcount=0):
        for i in range(self.number):
            a_out=self.a.fingerplay()
            b_out=self.b.fingerplay()
            print('第{}局比赛'.format(i+1))
            if a_out==b_out:
                print('双方平局,双方都出的是{}'.format(a_out))
            elif a_out=='石头' and b_out=='剪刀' or a_out=='剪刀' and b_out=='布' or a_out=='布' and b_out=='石头':
                acount+=1
                print('{}获得胜利，出的是{}，{}出的是{}'.format(self.a.name,a_out,self.b.name,b_out))
            else:
                bcount+=1
                print('{}获得胜利，出的是{}，{}出的是{}'.format(self.b.name,b_out,self.a.name,a_out))
        print('-'*35)
        if acount>bcount:
            print('{}获得最终胜利，得分{}'.format(self.a.name,acount))
        elif bcount>acount:
            print('{}获得最终胜利，得分{}'.format(self.b.name,bcount))
        else:
            print('双方平局，得分：{}'.format(acount))  

