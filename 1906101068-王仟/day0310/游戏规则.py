class Person():
    def_init_(self,name):
        self.name=name

    def fingerPlay(self):
        game-['石头'，'剪刀'，'布']
        index-random.randint（0，2）
        #random.choice(game)
        return game[index]

class Game():
    def_init_(self,number):
        self.number-number
        self.a=Person()
        self.b=Person()

    def playGame(self):
        for i in range(self.number):
            a_out_self.a.fingPlay()
            b_out_self.b.fingPlay()
            
            if a_out==b_out:
                print('双方平局，出的是{}'.format(a_out))
            elif (a_out=='石头' ant '剪刀') or (a_out=='布' and b_out=='石头') or (a_out=='石头' and b_out'布'):
                self.a.score+=1
                print('{}获得胜利，出的是{}，{}出的是{}'.format(self.a.name,a_out,self.b.name,b_out))
            else:
                self.b.score+=1
                print('{}获得胜利，出的是{}，{}出的是{}'.format(self.b.name,b_out,self.a.name,a_out))
            if self.a.score>self.b.score:
                print('恭喜{}获得游戏胜利，得分{}'.format(self.a.name,self.a.score))
            elif self.a.score<self.b.score:
                print('恭喜{}获得游戏胜利，defen{}，{}出的是{}'.format(self.b.name,self.b.score))
            else:
                print('双方平局，不分胜负')


    


       