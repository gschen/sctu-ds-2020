import random


class Person():
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def fingerPlay(self):
        game = ['剪刀','石头','布']
        index = random.randint(0, 2)
        return game[index]


class Game():
    def __init__(self, number, aname, bname):
        self.number = number
        self.a = Person(aname)
        self.b = Person(bname)
    
    def playGame(self):
        for i in range(self.number):
            a_out = self.a.fingerPlay()
            b_out = self.b.fingerPlay()
            if a_out == b_out:
                print('皆为{}--平局'.format(a_out))
            elif (a_out=='石头' and b_out=='剪刀') or (a_out=='剪刀' and b_out=='布') or (a_out=='布' and b_out=='石头'):
                self.a.score += 1
                print('{}为{}，{}为{}--{}胜利'.format(self.a.name, a_out, self.b.name, b_out, self.a.name))
            else:
                self.b.score += 1
                print('{}为{}，{}为{}--{}胜利'.format(self.a.name, a_out, self.b.name, b_out, self.b.name))
        if self.a.score > self.a.score:
            print('{}胜利{}次，获得最终胜利'.format(self.a.name, self.a.score))
        elif self.a.score < self.a.score:
            print('{}胜利{}次，获得最终胜利'.format(self.b.name, self.a.score))
        else:
            print('平局')

one = Game(5, '小明', '小红')
one.playGame()
