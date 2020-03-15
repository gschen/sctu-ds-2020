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

p1 = Player('P1', 200, 20, 0.5, 0.5)
p2 = Player('P2', 200, 20, 0.5, 0.5)
pp = Play()
pp.playGame()