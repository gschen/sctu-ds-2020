#角色PK

import random
class Player():
	def __init__(self,name,blood,attack,crit,DOD):
		self.name = name
		self.blood = blood
		self.attack = attack
		self.crit = crit
		self.DOD = DOD

	def role(self):
		print('玩家名称:%s\n血量:%s\n攻击力:%s\n暴击率:%s\n闪避率:%s' % (self.name,self.blood,self.attack,self.crit,self.DOD))
a=Player('路飞',1000,100,0.3,0.6)
b=Player('赤犬',2000,150,0.4,0.1)
a.role()
b.role()


import random
class Player():
	def __init__(self,name,blood,attack,crit,DOD):
		self.name = name
		self.blood = blood
		self.attack = attack
		self.crit = crit
		self.DOD = DOD
	def role(self):
		print('玩家名称:%s\n血量:%s\n攻击力:%s\n暴击率:%s\n闪避率:%s' % (self.name,self.blood,self.attack,self.crit,self.DOD))
class sb():
	def __init__(self):
		self.player1=a
		self.player2=b
	def playGame(self):
		print('游戏开始!')
		count=0
		while self.player1.blood >0 and self.player2.blood >0:
			count += 1
			if random.random() <= self.player1.crit:
				if random.random() <= self.player2.DOD:
					self.player2.blood -= 0
				else:
					self.player2.blood -= self.player1.attack * 2
			else:
				if random.random() <= self.player2.DOD:
					self.player2.blood -= 0
				else:
					self.player2.blood -= self.player1.attack

			if random.random() <= self.player2.crit:
				if random.random() <= self.player1.DOD:
					self.player1.blood -= 0
				else:
					self.player1.blood -= self.player2.attack * 2
			else:
				if random.random() <= self.player1.DOD:
					self.player2.blood -= 0
				else:
					self.player1.blood -= self.player2.attack
			if self.player1.blood <= 0:
				self.player1.blood = 0
			if self.player2.blood <= 0:
				self.player2.blood = 0
			print('第%d轮攻击:' % count)
			print('路飞:剩余血量: %d' % self.player1.blood)
			print('赤犬:剩余血量: %d' % self.player2.blood)
		if self.player1.blood == 0:
			print('经过%d轮攻击,赤犬成功击杀路飞,成为本局胜利者.' % count)
		else:
			print('经过%d轮攻击,路飞成功击杀赤犬,成为本局胜利者.' % count)
a=Player('路飞',1000,100,0.3,0.6)
b=Player('赤犬',2000,150,0.4,0.1)
c=sb()
c.playGame()

