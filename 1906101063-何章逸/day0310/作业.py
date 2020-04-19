#回合制人物Pk游戏
# 创建一个角色类(类)，包含属性有：角色名称、角色血量、攻击力、暴击率、闪避率。
# 创建一个游戏类，属性包含参加游戏的双方（对象），方法有playGame，参加游戏的双方互相攻击，可能产生暴击-----攻击力*2，可能闪避----闪避当前对方的攻击，直到一方血量<0，游戏结束。该方法打印每一轮游戏的情况，以及最终的获胜情况。

# 备注：如果暴击率是0.2可以用以下语句判断是否造成暴击
# if random.random() <= 0.2:
# 	pass

import random
class Character():
    def __init__(self,name,blood=100,attack,crit,DOD):
        self.name=name
        self.blood=blood
        self.attack=attack
        self.crit=crit
        self.DOD=DOD
        self.room=None
    def attach(self,other):
        fight={10:'物理攻击'}
        if self == other:
            print('不能攻击自己')
        else:
            if self.room and self.room == other.room:
                if self.blood <= 0:
                    print('您的血量低于0，不能进行攻击')
                else:
                    if ramdom.choice([0,1]) == 0:
                        lost_blood = random.choice([10,20])
                        print(f'{other.name}没有装备')
                    else:
                        lost_blood=random.choice([10,20])
                        print(f'{other.name}使用了装备')
                    other.blood = other.blood - lost_blood
                    print(f'{self.name}使用{fight[lost_blood]}攻击了{other.name}{lost_blood}点血量,当前血量{other.blood}')
                    if other.blood <= 0:
                        print(f'{other.name}已阵亡,不能再进行攻击')
                        exit()
            else：
                print('不在同一个房间不能攻击')


class Room(object):
    def __init__(self,name):
        self.name=name
        self.member_list = []
    def add_member(self,character):
        if character.room == None:
            if len(self.member_list) < 2:
                self.member_list.append(character)
                character.room = self
                print(f'{character.name}成功加入{self.name}房间')
        else:
            print(f'{character.name}已加入{character.room.name}房间')
print(############)

class Game():
    def __init__(self,blood=100,aattack,battack,acrit,bcrit,aDOD,bDOD,aname,bname):
        self.blood=blood
        self.a=Character(aattack)
        self.b=Character(battack)
        self.a=Character(acrit)
        self.b=Character(bcrit)
        self.a=Character(aDOD)
        self.b=Character(bDOD)
        self.a=Character(aname)
        self.b=Character(bname)
    
    def playGame():
        if aattack=(random.random())<=0.2 and battack=(random.random())>=0.2:
            print({self.a.name}攻击力不变,{self.b.name}攻击力变为原来2倍)
        else:
            print({self.a.naame}攻击力变为原来2倍,{self.b.name}攻击力不变)


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
Game()

        