import random
class Gameperson():
	def __init__(self,name,blood,attack,critical,miss):
		self.name=name
		self.blood=blood
		self.attack=attack
		self.critical=critical
		self.miss=miss
	def information(self):
		print('玩家名称:%s\n血量:%s\n攻击力:%s\n暴击率:%s\n闪避率:%s' % (self.name,self.blood,self.attack,self.critical,self.miss))

class Game():
	def __init__(self):
		self.playerA=a
		self.playerB=b
	def playGame(self):
		print('游戏开始!')
		count=0
		while self.playerA.blood>0 and self.playerB.blood>0:
			count += 1
			if random.random()<=self.playerA.critical:
				if random.random()<=self.playerB.miss:
					self.playerB.blood -=0
				else:
					self.playerB.blood -= self.playerA.attack * 2
			else:
				if random.random()<=self.playerB.miss:
					self.playerB.blood -= 0
				else:
					self.playerB.blood -= self.playerA.attack
			if random.random()<=self.playerB.critical:
				if random.random()<=self.playerA.miss:
					self.playerA.blood -= 0
				else:
					self.playerA.blood -= self.playerB.attack * 2
			else:
				if random.random()<=self.playerA.miss:
					self.playerB.blood -= 0
				else:
					self.playerA.blood -= self.playerB.attack
			if self.playerA.blood<=0:
				self.playerA.blood=0
			if self.playerA.blood<=0:
				self.playerB.blood=0
			print('第%d轮攻击:' % count)
			print('玩家A:剩余血量: %d' % self.playerA.blood)
			print('玩家B:剩余血量: %d' % self.playerB.blood)
		if self.playerA.blood == 0:
			print('经过{}轮攻击,玩家{}成功击玩家{},获胜'.format(count,self.playerA,self.playerB))
		else:
			print('经过{}轮攻击,玩家{}成功击玩家{},获胜'.format(count,self.playerB,self.playerA))

