# class Student():
#     def __init__(self,name,age,score):
#         self.name=name
#         self.age=age
#         self.score=score
#     def get_name(self):
#         print('姓名:',self.name)
#     def get_age(self):
#         print('年龄:',self.age)
#     def get_course(self):
#         print('最高分:',max(self.score))
# a=Student('Bob',18,[115,120,100])
# a.get_name()
# a.get_age()
# a.get_course()


#猜拳游戏
# import random
# class Person():
#     def __init__(self,name):
#         self.name=name
#         self.score=0
#     def fingerplay(self):
#         game=['石头','剪刀','布']
#         index=random.randint(0,2)
#         #random.choice(game)
#         return game[index]
    
# class Game():
#     def __init__(self,number,aname,bname):
#         self.number=number
#         self.a=Person(aname)
#         self.b=Person(bname)
#     def playgame(self):
#         for i in range(self.number):
#             a_out=self.a.fingerplay()
#             b_out=self.b.fingerplay()
#             if a_out==b_out:
#                 print('双方平局,出的是{}'.format(a_out))
#             elif (a_out=='石头' and b_out=='剪刀') or (a_out=='布' and b_out=='石头') or (a_out=='剪刀' and b_out=='布'):
#                 print('{}获得胜利，出的是{},{}出的是{}'.format(self.a.name,a_out,self.b.name,b_out))
#                 self.a.score+=1
#             else:
#                 print('{}获得胜利，出的是{},{}出的是{}'.format(self.b.name,b_out,self.a.name,a_out))
#                 self.b.score+=1
#         if self.a.score>self.b.score:
#             print('恭喜{}获得胜利,得分:{}'.format(self.a.name,self.a.score))
#         elif self.a.score<self.b.score:
#             print('恭喜{}获得胜利,得分:{}'.format(self.b.name,self.b.score))
#         else:
#             print("双方平局，不分胜负")  
# one=Game(600,'甲方','乙方')
# one.playgame()



            
        
