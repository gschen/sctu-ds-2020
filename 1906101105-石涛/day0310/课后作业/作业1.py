# coding=utf-8

'''
回合制人物Pk游戏
创建一个角色类(类)，包含属性有：角色名称、角色血量、攻击力、暴击率、闪避率。
创建一个游戏类，属性包含参加游戏的双方（对象），方法有playGame，参加游戏的
双方互相攻击，可能产生暴击-----攻击力*2，可能闪避----闪避当前对方的攻击，直
到一方血量<0，游戏结束。该方法打印每一轮游戏的情况，以及最终的获胜情况。

备注：如果暴击率是0.2可以用以下语句判断是否造成暴击
if random.random() <= 0.2:
	pass
'''

import random

class Character():
    def __init__(self,Blood_volume,Aggressivity,Critical_hit_rate,Evade,name):
        self.Blood_volume=Blood_volume
        self.Aggressivity=Aggressivity
        self.Critical_hit_rate=Critical_hit_rate
        self.Evade=Evade
        self.name=name
    def play_A(self):
        skills_A=['八极崩','焰分噬浪尺','六合游身尺','三千雷动','佛怒火莲','佛怒轮回','异火恒古尺']
        index=random.randint(0,6)
        return [index,skills_A[index]]
    def play_B(self):
        skills_B=['七伤拳','一阳指','大力金刚拳','九阴白骨爪','六脉神剑','独孤九剑','如来神掌']
        index=random.randint(0,6)
        return [index,skills_B[index]]

class Game():
    def __init__(self,Role_name):
        self.a=Character(random.randint(20000,22000),random.randint(800,1000),(random.randint(1,5))/10,(random.randint(1,2))/10,Role_name)
        self.b=Character(random.randint(20000,22000),random.randint(800,1000),(random.randint(1,5))/10,(random.randint(1,2))/10,'神秘敌人')
    def palyGame(self):
        n=0
        print('你被来历不明的敌人追杀！！！\n却偶然跌落到了一片神秘空间.\n这里充满了各种不同颜色的火焰.\n')
        print('这里的一位神秘强者说与你有缘，便让你吞噬了这里的所有火焰.\n并且学会了这位强者的所有技能....\n')
        print('此时你已经很强大了！！！\n现在你回到原来的世界...')
        print('-'*30)
        print('不巧，神秘人却找到了你！！！\n此时的你们的数据是：\n')
        print('{:^10}{:^12}'.format(self.a.name,self.b.name))
        print('生命值：{:<6}生命值：{:<6}\n攻击力：{:<6}攻击力：{:<6}\n暴击率：{:<6}暴击率：{:<6}\n闪避率：{:<6}闪避率：{:<6}\n'.format(self.a.Blood_volume,self.b.Blood_volume,self.a.Aggressivity,self.b.Aggressivity,self.a.Critical_hit_rate,self.b.Critical_hit_rate,self.a.Evade,self.b.Evade))
        print('-'*20)
        x=input('你是否需要对战？(请填是或否)：')
        if x=='否':
            print('你向身后逃去！！！但神秘敌人却追了上来！！！')
        print('\n你们见面便对上了！！！\n战斗一触即发！！！\n')
        while True:
            a_out=self.a.play_A()
            b_out=self.b.play_B()
            n+=1
            print('第{}回合'.format(n))
            m=input('你是进攻还是防守？(请输入1-->(进攻)或2-->(防守))')
            if m=='1':
                if self.b.Evade>=random.random():
                    print('{}使出了一招{}，但{}身形一闪，躲避了{}！！！'.format(self.a.name,a_out[1],self.b.name,a_out[1]))
                else:
                    if self.b.Critical_hit_rate>=random.random():
                        print('{}使出了一招{}，击中了{}的要害，造成{}点伤害！！！'.format(self.a.name,a_out[1],self.b.name,(a_out[0]+1)*self.a.Aggressivity*2))
                        self.b.Blood_volume-=(a_out[0]+1)*self.a.Aggressivity*2
                    else:
                        print('{}使出了一招{}，对{}造成了{}点伤害！'.format(self.a.name,a_out[1],self.b.name,(a_out[0]+1)*self.a.Aggressivity))
                        self.b.Blood_volume-=(a_out[0]+1)*self.a.Aggressivity
            if m=='2':
                self.a.Evade+=0.5

            if self.a.Evade>=random.random():
                if m=='2':
                    print('{}使出了一招{}，但{}身形一闪，躲避了{}，并且回身一击对{}造成800点伤害！！！'.format(self.b.name,b_out[1],self.a.name,b_out[1],self.b.name))
                    self.b.Blood_volume-=800
                else:
                    print('{}使出了一招{}，但{}身形一闪，躲避了{}！！！'.format(self.b.name,b_out[1],self.a.name,b_out[1]))
            else:
                if self.a.Critical_hit_rate>=random.random():
                    print('{}使出了一招{}，击中了{}的要害，造成{}点伤害！！！'.format(self.b.name,b_out[1],self.a.name,(b_out[0]+1)*self.a.Aggressivity))
                    self.a.Blood_volume-=((b_out[0]+1)*self.b.Aggressivity)*2
                else:
                    print('{}使出了一招{}，对{}造成了{}点伤害！'.format(self.b.name,b_out[1],self.a.name,((b_out[0]+1)*self.b.Aggressivity)/2))
                    self.a.Blood_volume-=((b_out[0]+1)*self.b.Aggressivity)
            if m=='2':
                self.a.Evade-=0.5

            if self.b.Blood_volume<=0:
                print('-'*60)
                print('\n--战斗结束--\n--你战胜了敌人！！！--\n')
                print('神秘敌人：你怎么会这么短的时间变得如此之强！！！\n     ......看来我是无法保护这个世界了！')
                print('{}：什么保护世界！你为什么要杀我？！'.format(self.a.name))
                print('神秘敌人：因为你是....\n在他话还未说完，便没了声息......')
                print('{}：我是？...我是什么啊？！...你快给我说完啊！！！'.format(self.a.name))
                print('{}望向远方，不断思索着......\n不管怎样，我得去找下答案！！！\n{}的身影消失在了虚空中......'.format(self.a.name,self.a.name))
                break
            elif self.a.Blood_volume<=0:
                print('-'*60)
                print('\n--战斗结束--\n--你被敌人打败了！！！--\n')
                print('{}：为什么？！！...为什么你要杀我？！！！'.format(self.a.name))
                print('神秘敌人：因为你本不该来到这个世界......\n抛下这句话，神秘敌人转身离去...\n{}的身体消散在了空中...'.format(self.a.name))
                break

st=Game('ST-one')
st.palyGame()