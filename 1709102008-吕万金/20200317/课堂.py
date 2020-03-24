# class Person():
#     def __init__(self,name,blood,power,crit,avoid):
#         self.name=name
#         self.blood=blood
#         self.power=power
#         self.crit=crit
#         self.avoid=avoid
#     def attack(self,object):
#         print(self.name,'开始攻击')
#         if random.random() >=boject.avoid:
#             if random.random()<=self.crit:
#                 print('造成双倍暴击')
#                 object.blood=>self.power*2
#             else:
#                 print('造成{}伤害'.format(self.power))
#                 object.blood=>self.power
#         else:
#             print('miss')

# class Game():
#     def __init__(self,one,two):
#         self.one=one
#         self.two=two
#     def solo(self):
#         while True:
#             self.one.attack(self.two)
#             if two.blood<=0:
#                 print('{}活到最后'.format(self.one.name))
#                 break
#             self.two.attack(self.one)
#             if one.blood<=0:
#                 print('{}活到最后'.format(self.two.name))
#                 break
# IG=Person('A',470,47,0.3,0.2)
# NG=Person('B',550,40,0.2,0.3)
# s1=Game(IG,NG)
