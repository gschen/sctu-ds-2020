import random
class Person():
    def __init__(self,name):
        self.name = name

    def fingerplay(self):
        game = ['剪刀','石头','布']
        index = random.randint(0,2)
        #random.choice(game)
        return game[index]


class Game():
    def __init__(self,number,a,b):
        self.number = number
        self.a = Person(a)
        self.b = Person(b)


    def playgame(self):
        for i in range(self.number):
            a_out = self.a.fingerplay()
            b_out = self.b.fingerplay()
            if a_out == b_out:
                print('双方都为{}，平局'.format(a_out))
            elif (a_out == '石头' and b_out == '剪刀') or (a_out == '剪刀' and b_out == '布') or (a_out == '布' and b_out == '石头'):
                print('{}获胜,出的是{}，而{}出的是{}'.format(self.a.name,a_out,self.b.name,b_out))
            else:
                print('{}获胜,出的是{}，而{}出的是{}'.format(self.b.name,b_out,self.a.name,a_out))
start = Game(3,'Tom','Jerry')
start.playgame()