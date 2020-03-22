import random
class Role():
	def __init__(self,name,blood,attack,violence,dodge):
		self.name=name
		self.blood=blood
		self.attack=attack
		self.violence=violence
		self.dodge=dodge
	def information(self):
		print('玩家名称:%s\n血量:%s\n攻击力:%s\n暴击率:%s\n闪避率:%s' % (self.name,self.blood,self.attack,self.violence,self.dodge))
class Game():
	def __init__(self):
		self.player1=a
		self.player2=b
	def playGame(self):
		print('游戏开始!')
		count = 0
		while self.player1.blood>0 and self.player2.blood>0:
			count += 1
			if random.random()<=self.player1.violence:
				if random.random()<=self.player2.dodge:
					self.player2.blood -=0
				else:
					self.player2.blood -= self.player1.attack * 2
			else:
				if random.random()<=self.player2.dodge:
					self.player2.blood -= 0
				else:
					self.player2.blood -= self.player1.attack
			if random.random()<=self.player2.violence:
				if random.random()<=self.player1.dodge:
					self.player1.blood -= 0
				else:
					self.player1.blood -= self.player2.attack * 2
			else:
				if random.random()<=self.player1.dodge:
					self.player2.blood -= 0
				else:
					self.player1.blood -= self.player2.attack
			if self.player1.blood<=0:
				self.player1.blood=0
			if self.player2.blood<=0:
				self.player2.blood=0
			print('第{}轮攻击:'.format(count))
			print('A:剩余血量:{}'.format(self.player1.blood))
			print('B:剩余血量: {}'.format(self.player2.blood))
		if self.player1.blood == 0:
			print('经过{}轮攻击,B成为本局胜利者'.format(count))
		else:
			print('经过{}轮攻击,A成为本局胜利者'.format(count))
a=Role('A',1000,100,0.4,0.6)
b=Role('B',2000,50,0.1,0.1)
c=Game()
c.playGame()


# import random
# class Person():
#     def __init__(self,name,blood,power,crit,avoid):
#         self.name=name
#         self.blood=blood
#         self.power=power
#         self.crit=crit
#         self.avoid=avoid
#     #攻击
#     def attack(self,object):
#         print(self.name,'开始攻击')
#         #对方是否闪避本次攻击
#         #表示我方命中
#         if random.random() >=object.avoid:
#             #判断是否暴击
#             if random.random() <=self.crit:
#                 print('------造成双倍伤害')
#                 object.blood-=self.power*2
#             else:
#                 print('------造成{}伤害'.format(self.power))
#                 object.blood-=self.power
#         else:
#             print('-------miss')

# class Game():
#     def __init__(self,one,two):
#         #导入solo双方
#         self.one=one
#         self.two=two
#     def solo(self):
#         while True:
#             self.one.attack(self.two)
#             if self.two.blood<=0:
#                 print('{}活到了最后'.format(self.one.name))
#                 break
#             self.two.attack(self.one)
#             if self.one.blood<=0:
#                 print('{}活到了最后'.format(self.two.name))
#                 break

# lg=Person('A',470,47,0.3,0.2)
# jj=Person('B',550,40,0.2,0.3)
# sl=Game(lg,jj)
# sl.solo()