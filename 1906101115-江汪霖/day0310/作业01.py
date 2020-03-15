import random
class Geren():
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
		print('游戏开始！')


