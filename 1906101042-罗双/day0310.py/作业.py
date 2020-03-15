# #回合制人物Pk游戏
# 创建一个角色类(类)，包含属性有：角色名称、角色血量、攻击力、暴击率、闪避率。
# 创建一个游戏类，属性包含参加游戏的双方（对象），方法有playGame，参加游戏的双方互相攻击，可能产生暴击-----攻击力*2，可能闪避----闪避当前对方的攻击，直到一方血量<0，游戏结束。该方法打印每一轮游戏的情况，以及最终的获胜情况。

# 备注：如果暴击率是0.2可以用以下语句判断是否造成暴击
# if random.random() <= 0.2:
# 	pass
import random
class Action():
    def __init__(self,name,blood,power,strike,dodge):
        self.name=name
        self.blood=blood
        self.power=power
        self.strike=strike
        self.dodge=dodge
    
class Game():
    def __init__(self,aname,bname):
        self.a=aname
        self.b=bname
    def playGame(self):
        print('开始')
        n=1
        while self.a.blood>0 and self.b.blood>0:
            c=input('输入1开始一次互相伤害：')
            print('第{}回合开始'.format(n))
            a=1
            b=1
            while a==1:
                if random.random()<=self.b.dodge:          

