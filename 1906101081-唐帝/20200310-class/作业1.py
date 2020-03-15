import random
class Role(object):
	def __init__(self,name,sex,blood=100):
		self.name = name
		self.sex = sex
		self.blood = blood
		self.room = None
	def attach(self,other):
		fight = {10:"物理攻击",20:"魔法攻击"}
		if self == other:
			print("不能攻击自己")
		else:
			if self.room and self.room == other.room:
				if self.blood <= 0:
					print("您的血量低于0，不能进行攻击")
				else:
					if random.choice([0,1]) == 0:
						lost_blood = random.choice([10,20])
						print(f"{other.name}没有装备")
					else:
						lost_blood = random.choice([10,20])
						print(f"{other.name}使用了装备")
					other.blood = other.blood - lost_blood
					print(f"{self.name}使用{fight[lost_blood]}攻击了{other.name}{lost_blood}点血量，当前血量{other.blood}")
					if other.blood <= 0:
						print(f"{other.name}已阵亡，不能再进行攻击")
						exit()
			else:
				print("不在同一个房间不能攻击")