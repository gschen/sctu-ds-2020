import random
class Role(object):
	def __init__(self,name,blood=100,damage,crit,Dodge rate):
		self.name = name
		self.blood = blood
		self.damage = damage
		self.crit = crit
        self.Dodge rate = Dodge rate
        self.room = None
	def attach(self,other):
    		fight = {10:"物理攻击",20:"魔法攻击"}
		if self == other:
			print("不能攻击自己")
		else:
			if self.room and self.room == other.room:
				if self.blood <= 0:
					print("您的血量低于0，不能进行攻击")
				if other.blood <= 0:
    						print(f"{other.name}已阵亡，不能再进行攻击")
						exit()
				else:
					print("不在同一个房间不能攻击")
class Room(object):
	def __init__(self,name):
		self.name = name
		self.member_list = []
	def add_member(self,role):
		if role.room == None:
			if len(self.member_list) < 2:
				self.member_list.append(role)
				role.room = self
				print(f"{role.name}成功加入{self.name}房间")
		else:
			print(f"{role.name}已加入{role.room.name}房间")
print('''################
1.创建角色
2.创建房间
3.加入房间
4.开始战斗
5.退出
################''')
roles = dict()
rooms = dict()
while True:
	enter_number = input("请输入您的操作：\n")
	if enter_number.isdigit():
		enter_number = int(enter_number)
		if 1 <= enter_number <= 5:
			if enter_number == 1:
				name,sex = input("请输入角色的姓名与性别，空格分隔：\n").split()
				roles[name] = Role(name,sex)
			elif enter_number == 2:
				room = input("请输入房间的名字：\n")
				rooms[room] = Room(room)
			elif enter_number == 3:
				print(f"当前角色有{roles.keys()}，当前房间有{rooms.keys()}")
				role_name,room_name = input("请输入您要加入的角色和房间名，空格分隔:\n").split()
				rooms[room_name].add_member(roles[role_name])
			elif enter_number == 4:
				while True:
					enter = random.choice([0,1])
					if enter == 0:							
						rooms[room_name].member_list[0].attach(rooms[room_name].member_list[1])
					else:
						rooms[room_name].member_list[1].attach(rooms[room_name].member_list[0])					
		else:
			print("输入错误！请输入1-5选择操作！")
	else:
		print("输入有误！请重新输入！")

        