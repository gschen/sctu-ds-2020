'''回合制人物Pk游戏
创建一个角色类(类)，包含属性有：角色名称、角色血量、攻击力、暴击率、闪避率。
创建一个游戏类，属性包含参加游戏的双方（对象），方法有playGame，参加游戏的双方互相攻击，可能产生暴击-----攻击力*2，可能闪避----闪避当前对方的攻击，直到一方血量<0，游戏结束。该方法打印每一轮游戏的情况，以及最终的获胜情况。

备注：如果暴击率是0.2可以用以下语句判断是否造成暴击
if random.random() <= 0.2:
	pass'''

class Gameperson():
	def __init__(self,name,blood,attack,violence,dodge):
		self.name=name
		self.blood=blood
		self.attack=attack
		self.violence=violence
		self.dodge=dodge
	def information(self):
		print('玩家名称:%s\n血量:%s\n攻击力:%s\n暴击率:%s\n闪避率:%s' % (self.name,self.blood,self.attack,self.violence,self.dodge))
a=Gameperson('妲己',1000,100,0.4,0.6)
b=Gameperson('安琪拉',2000,50,0.1,0.1)
a.information()
b.information()

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
class Jia():
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
			print('妲己:剩余血量: %d' % self.player1.blood)
			print('安琪拉:剩余血量: %d' % self.player2.blood)
		if self.player1.blood == 0:
			print('经过%d轮攻击,安琪拉成功击杀大头,成为本局胜利者.' % count)
		else:
			print('经过%d轮攻击,妲己成功击杀BOSS,成为本剧胜利者.' % count)
a=Gameperson('妲己',1000,100,0.4,0.6)
b=Gameperson('安琪拉',2000,50,0.1,0.1)
c=Jia()
c.playGame()
