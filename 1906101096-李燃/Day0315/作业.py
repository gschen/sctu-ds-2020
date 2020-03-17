# 回合制人物Pk游戏
# 创建一个角色类(类)，包含属性有：角色名称、角色血量、攻击力、暴击率、闪避率。
# 创建一个游戏类，属性包含参加游戏的双方（对象），方法有playGame，参加游戏的双方互相攻击，可能产生暴击-----攻击力*2，可能闪避----闪避当前对方的攻击，直到一方血量<0，游戏结束。该方法打印每一轮游戏的情况，以及最终的获胜情况。

# 备注：如果暴击率是0.2可以用以下语句判断是否造成暴击
# if random.random() <= 0.2:
# 	pass

#hp 血量；att 攻击力；per 暴击率；spd 闪避


import random
class Role():
    def __init__(self,name,hp,att,per,spd):
        hp= random.randint(100,200)
        att= random.randint(10,20)
        self.name=name
        self.hp=hp
        self.att=att
        self.per=per
        self.spd=spd
    def personinfo(self):
        print(('角色名称:%s,角色血量:%s,攻击力:%s,暴击率:%s,闪避率:%s')%(self.name,self.hp,self.att,self.per,self.spd))

class Game():
    def __init__(self,aname,bname,ahp,bhp,aatt,batt):
        self.a=Role(aname)
        self.b=Role(bname)


    def playGame(self):
        print('游戏开始')
        for i in range(5):
            print('----现在开始第%s回合' % i)
            ahp= random.randint(100,200)
            aatt= random.randint(10,20)
            bhp = random.randint(100,150)
            batt = random.randint(10,22)
            print('玩家1： \n血量：%s \n攻击%d' % (self.a.hp,self.a.att))
            print('玩家2： \n血量：%s \n攻击%d' % (self.b.hp,self.b.att))

        while (a.hp)>0 and (b.hp>0):
             a.hp=a.hp-b.att
             b.hp=b.hp-a.att
             print('玩家1：\n剩余血量：%s\n攻击%d' % (self.a.hp,self.a.att))
             print('玩家2：\n剩余血量：%s\n攻击%d' % (self.b.hp,self.b.att))

             if ahp>0 and bhp<0:
                print('耶，你赢了!')
                a.hp+=1
             elif ahp<0 and bhp>0:
                print('哦豁！你输掉了!')
                b.hp+=1
             elif ahp<0 and bhp<0:
                print('都死掉了!!')

a = Role('玩家1',120,15,0.1,0.1)
b = Role('玩家2',100,20,0.1,0.2)
one= Game(a,b)
one.playGame()


        