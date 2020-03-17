'''回合制人物Pk游戏
创建一个角色类(类)，包含属性有：角色名称、角色血量、攻击力、暴击率、闪避率。
创建一个游戏类，属性包含参加游戏的双方（对象），方法有playGame，参加游戏的双方互相攻击，
可能产生暴击-----攻击力*2，可能闪避----闪避当前对方的攻击，直到一方血量<0，游戏结束。
该方法打印每一轮游戏的情况，以及最终的获胜情况。
备注：如果暴击率是0.2可以用以下语句判断是否造成暴击
if random.random() <= 0.2:
	pass
'''
import random

class Player():
	def __init__(self, name, HP, Attack, Crit, Dodge):
		self.name = name
		self.HP = HP
		self.Attack = Attack
		self.Crit = Crit
		self.Dodge = Dodge
class Play():
	def __init__(self):
		self.yc = yc
		self.cc = cc
	def playGame(self):
		count = 0
		while self.yc.HP > 0 and self.cc.HP > 0:
			count += 1
			print('第{}回合:'.format(count))

			if random.random() <= self.cc.Dodge:
				self.cc.HP -= 0
				print('{}闪避了{}的攻击'.format(self.cc.name, self.yc.name))
			else:
				if random.random() <= self.yc.Crit:
					self.cc.HP -= self.yc.Attack * 2
					print('{}对{}的攻击造成了暴击'.format(self.yc.name, self.cc.name))
				else:
					self.cc.HP -= self.yc.Attack

			if random.random() <= self.yc.Dodge:
				self.yc.HP -= 0
				print('{}闪避了{}的攻击'.format(self.yc.name, self.cc.name))
			else:
				if random.random() <= self.cc.Crit:
					self.yc.HP -= self.cc.Attack * 2
					print('{}对{}的攻击造成了暴击'.format(self.cc.name, self.yc.name))
				else:
					self.yc.HP -= self.cc.Attack

			if self.yc.HP < 0:
				self.yc.HP = 0
			if self.cc.HP < 0:
				self.cc.HP = 0
			
			print('{}剩余血量:{}'.format(self.yc.name, self.yc.HP))
			print('{}剩余血量:{}'.format(self.cc.name, self.cc.HP))
		print('--------------------------------------------')
		if self.yc.HP == 0 and self.cc.HP == 0:
			print('{}和{}在第{}个回合后同归于尽'.format(self.cc.name, self.yc.name, count))
		elif self.yc.HP == 0 and self.cc.HP != 0:
			print('{}在第{}个回合击杀{},获得胜利'.format(self.cc.name, count, self.yc.name))
		else:
			print('{}在第{}个回合击杀{},获得胜利'.format(self.yc.name, count, self.cc.name))

yc = Player('yc', 100, 10, 0.2, 0.2)
cc = Player('cc', 100, 10, 0.2, 0.2)
ll = Play()
ll.playGame()