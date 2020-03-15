#创建一个游戏类，属性包含参加游戏的双方（对象），方法有playGame，参加游戏的双方互相攻击，可能产生暴击-----攻击力*2，可能闪避----
# 闪避当前对方的攻击，直到一方血量<0，游戏结束。该方法打印每一轮游戏的情况，以及最终的获胜情况。



import random
class Role():
	def __init__(self,name,life,fight,crit,dodge):
		self.name=name
		self.life=life
		self.fight=fight
		self.crit=crit
		self.dodge=dodge
	def information(self):
		print('玩家名称:%s\n血量:%s\n攻击力:%s\n暴击率:%s\n闪避率:%s' % (self.name,self.life,self.fight,self.crit,self.dodge))
class Qin():
	def __init__(self):
		self.player1=a
		self.player2=b
	def playGame(self):
		print('游戏开始!')
		count=0
		while self.player1.life>0 and self.player2.life>0:
			count += 1
			if random.random()<=self.player1.fight:
				if random.random()<=self.player2.dodge:
					self.player2.life -=0
				else:
					self.player2.life -= self.player1.fight * 2
			else:
				if random.random()<=self.player2.dodge:
					self.player2.life -= 0
				else:
					self.player2.life -= self.player1.fight
			if random.random()<=self.player2.crit:
				if random.random()<=self.player1.dodge:
					self.player1.life -= 0
				else:
					self.player1.life -= self.player2.fight * 2
			else:
				if random.random()<=self.player1.dodge:
					self.player2.life -= 0
				else:
					self.player1.life -= self.player2.fight
			if self.player1.life<=0:
				self.player1.life=0
			if self.player2.life<=0:
				self.player2.life=0
			print('第%d轮攻击:' % count)
			print('秦驰:剩余血量: %d' % self.player1.life)
			print('花户:剩余血量: %d' % self.player2.life)
		if self.player1.life == 0:
			print('经过%d轮攻击,花户成功击杀秦驰,成为本局胜利者.' % count)
		else:
			print('经过%d轮攻击,秦驰成功击杀花户,成为本剧胜利者.' % count)
a=Role('秦驰',1000,100,0.4,0.6)
b=Role('花户',2000,50,0.1,0.1)
c=Qin()
c.playGame()


