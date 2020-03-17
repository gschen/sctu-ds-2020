'''
class Student():

    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)

    def get_course(self):
        print(max(self.score))

my_info = Student('dzm',19,[58,59,61])
my_info.get_name()
my_info.get_age()
my_info.get_course()
'''
import random
class Person():
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def fingerplay(self):
        game = ['剪刀','石头','布']
        index = random.randint(0,2)
        #random.choice(game)
        return game[index]


class Game():
    def __init__(self,number,a,b):#a,b就是传入两个人的名字，用来记录一下
        self.number = number
        self.a = Person(a,0)
        self.b = Person(b,0)


    def playgame(self):
        for i in range(self.number):
            a_out = self.a.fingerplay()
            b_out = self.b.fingerplay()
            if a_out == b_out:
                print('双方都为{}，平局'.format(a_out))
            elif (a_out == '石头' and b_out == '剪刀') or (a_out == '剪刀' and b_out == '布') or (a_out == '布' and b_out == '石头'):
                print('{}获胜,出的是{}，而{}出的是{}'.format(self.a.name,a_out,self.b.name,b_out))
                self.a.score += 1
            else:
                print('{}获胜,出的是{}，而{}出的是{}'.format(self.b.name,b_out,self.a.name,a_out))
                self.b.score += 1
        print('{}得{}分，{}得{}分'.format(self.a.name,self.a.score,self.b.name,self.b.score))

start = Game(300,'傻逼一号','傻逼二号')
start.playgame()

