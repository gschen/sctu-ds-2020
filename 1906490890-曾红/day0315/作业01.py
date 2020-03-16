# 回合制人物Pk游戏
# 创建一个角色类(类)，包含属性有：角色名称、角色血量、攻击力、暴击率、闪避率。
# 创建一个游戏类，属性包含参加游戏的双方（对象），方法有playGame，参加游戏的双方互相攻击，可能产生暴击-----攻击力*2，可能闪避----闪避当前对方的攻击，直到一方血量<0，游戏结束。该方法打印每一轮游戏的情况，以及最终的获胜情况。

# 备注：如果暴击率是0.2可以用以下语句判断是否造成暴击
# if random.random() <= 0.2:
# 	pass


import random
class Player():
 	def __init__(self,name,blood,attack,bj,ds):
 		self.name = name
 		self.blood = blood
 		self.attack = attack
 		self.bj = bj
 		self.ds = ds

 	def role(self):
 		print('玩家:%s\n血量:%s\n攻击力:%s\n暴击率:%s\n闪避率:%s' % (self.name,self.blood,self.attack,self.bj,self.ds))
a=Player('bob',100,50,0.2,0.6)
b=Player('cc',2000,150,0.4,0.1)
a.role()
b.role()