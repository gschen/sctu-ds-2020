import random
class Gameperson():
	def __init__(self,name,blood,attack,violence,dodge):
		self.name=name
		self.blood=blood
		self.attack=attack
		self.violence=violence
		self.dodge=dodge
	def information(self):
		print('玩家名称:%s\n血量:%s\n攻击力:%s\n暴击率:%s\n闪避率:%s' % (self.name,self.blood,self.attack,self.violence,self.dodge))
a=Gameperson('斩星',200,100,10,10)
b=Gameperson('掠星',100,50,0.5,0.5)
class hukan():
	def __init__(self):
		self.player1=a
		self.player2=b
	def playGame(self):
		print('游戏开始!')
		count=0
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
			print('第%d轮攻击:' % count)
			print('斩星:剩余血量: %d' % self.player1.blood)
			print('掠星:剩余血量: %d' % self.player2.blood)
		if self.player1.blood == 0:
			print('经过%d轮攻击,掠星成功击杀斩星,成为游戏胜利者.' % count)
		else:
			print('经过%d轮攻击,斩星成功击杀掠星,成为游戏胜利者.' % count)
a=Gameperson('斩星',1200,80,0.2,0.7)
b=Gameperson('掠星',2000,60,0.2,0.5)
c=hukan()
c.playGame()