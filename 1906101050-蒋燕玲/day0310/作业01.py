# 回合制人物Pk游戏
# 创建一个角色类(类)，包含属性有：角色名称、角色血量、攻击力、暴击率、闪避率。
# 创建一个游戏类，属性包含参加游戏的双方（对象），方法有playGame，参加游戏的双方互相攻击，可能产生暴击-----攻击力*2，可能闪避----闪避当前对方的攻击，直到一方血量<0，游戏结束。该方法打印每一轮游戏的情况，以及最终的获胜情况。

# 备注：如果暴击率是0.2可以用以下语句判断是否造成暴击
# if random.random() <= 0.2:
import random

class Player():
	def __init__(self, name, hp, attack, crit, dodge):
		self.name = name
		self.hp = hp
		self.attack = attack
		self.crit = crit
		self.dodge = dodge
class Play():
	def __init__(self):
		self.p1 = p1
		self.p2 = p2
	def playGame(self):
		count = 0
		while self.p1.hp > 0 and self.p2.hp > 0:
			count += 1
			print('第{}回合:'.format(count))

			if random.random() <= self.p2.dodge:
				self.p2.hp -= 0
				print('{}闪避了{}的攻击'.format(self.p2.name, self.p1.name))
			else:
				if random.random() <= self.p1.crit:
					self.p2.hp -= self.p1.attack * 2
					print('{}对{}的攻击造成了暴击'.format(self.p1.name, self.p2.name))
				else:
					self.p2.hp -= self.p1.attack

			if random.random() <= self.p1.dodge:
				self.p1.hp -= 0
				print('{}闪避了{}的攻击'.format(self.p1.name, self.p2.name))
			else:
				if random.random() <= self.p2.crit:
					self.p1.hp -= self.p2.attack * 2
					print('{}对{}的攻击造成了暴击'.format(self.p2.name, self.p1.name))
				else:
					self.p1.hp -= self.p2.attack

			if self.p1.hp < 0:
				self.p1.hp = 0
			if self.p2.hp < 0:
				self.p2.hp = 0
			
			print('{}剩余血量:{}'.format(self.p1.name, self.p1.hp))
			print('{}剩余血量:{}'.format(self.p2.name, self.p2.hp))
		print('--------------------------------------------')
		if self.p1.hp == 0 and self.p2.hp == 0:
			print('{}和{}在第{}个回合后同归于尽'.format(self.p2.name, self.p1.name, count))
		elif self.p1.hp == 0 and self.p2.hp != 0:
			print('{}在第{}个回合击杀{},获得胜利'.format(self.p2.name, count, self.p1.name))
		else:
			print('{}在第{}个回合击杀{},获得胜利'.format(self.p1.name, count, self.p2.name))

p1 = Player('张三', 100, 10, 0.25, 0.25)
p2 = Player('李四', 100, 10, 0.25, 0.25)
pp = Play()
pp.playGame()
