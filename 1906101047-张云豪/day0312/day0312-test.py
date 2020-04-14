import random
class Role():
    def __init__(self,name,blood,attact,crit,miss):
        self.name=name
        self.blood=blood
        self.attact=attact
        self.crit=crit
        self.miss=miss


    # def miss(self):
    #     self.miss=self.miss
    # def blood(self):
    #     self.blood=self.blood
    # def attact(self):
    #     self.attact=self.attact
    # def crit(self):
    #     self.crit=self.crit

class Game():
    def __init__(self,aname,bname):
        self.aname=aname
        self.bname=bname

    def playGame(self):
        g=random.randint(0,1)
        num=1
        while g==1:
            if num==1:
                print('第%s回合%s率先开啥攻击'%(num,a.name))
                print('\n')
            else:
                print('第%s回合'%(num))
                print('\n')
            num=num+1
            if random.random()<=a1.miss:
                a1.blood=a1.blood


                if a.name=='压缩':
                    l=['地爆天星','神罗天征']
                    i=random.randint(0,1)
                    print('{}使出了{}'.format(a.name,l[i]))
                if a.name=='塞拉斯':
                    l1=['真数火影千手','仙术·明神门']
                    i1=random.randint(0,1)
                    print('{}使出了{}'.format(a.name,l1[i1]))
                if a.name=='vn':
                    l2=['六道阴阳遁手里剑','大玉螺旋丸']
                    i2=random.randint(0,1)
                    print('{}使出了{}'.format(a.name,l2[i2]))
                if a.name=='卡萨丁':
                    l3=['别天神','月读']
                    i3=random.randint(0,1)
                    print('{}使出了{}'.format(a.name,l3[i3])) 






                if a1.name=='压缩':
                    print('{}使出了须佐能乎挡住了攻击'.format(a1.name))
                    print ("\n"*2)
                if a1.name=='塞拉斯':
                    print('{}使出了五重罗生门挡住了攻击'.format(a1.name))
                    print ("\n"*2)
                if a1.name=='vn':
                    print('{}使出了尾兽查克拉外衣挡住了攻击'.format(a1.name))
                    print ("\n"*2)
                if a1.name=='卡萨丁':
                    print('{}使出了加具土命挡住了攻击'.format(a1.name))
                    print ("\n"*2)


                if random.random()<=a.miss:



                    if a1.name=='压缩':
                        l=['地爆天星','神罗天征']
                        i=random.randint(0,1)
                        print('{}使出了{}'.format(a1.name,l[i]))
                    if a1.name=='塞拉斯':
                        l1=['真数火影千手','仙术·明神门']
                        i1=random.randint(0,1)
                        print('{}使出了{}'.format(a1.name,l1[i1]))
                    if a1.name=='vn':
                        l2=['六道阴阳遁手里剑','大玉螺旋丸']
                        i2=random.randint(0,1)
                        print('{}使出了{}'.format(a1.name,l2[i2]))
                    if a1.name=='卡萨丁':
                        l3=['别天神','月读']
                        i3=random.randint(0,1)
                        print('{}使出了{}'.format(a1.name,l3[i3])) 



                if a.name=='压缩':
                    print('{}使出了须佐能乎挡住了攻击'.format(a.name))
                    print ("\n"*2)
                if a.name=='塞拉斯':
                    print('{}使出了五重罗生门挡住了攻击'.format(a.name))
                    print ("\n"*2)
                if a.name=='vn':
                    print('{}使出了尾兽查克拉外衣挡住了攻击'.format(a.name))
                    print ("\n"*2)
                if a.name=='卡萨丁':
                    print('{}使出了加具土命挡住了攻击'.format(a.name))
                    print ("\n"*2)
                    a.blood=a.blood


                else:
                    if random.random()<=a1.crit:
                        if a1.name=='压缩':
                            print('{}使出了地爆天星，对方受到伤害'.format(a1.name))
                            print ("\n"*2)
                        if a1.name=='塞拉斯':
                            print('{}使出了真数火影千手，对方受到伤害'.format(a1.name))
                            print ("\n"*2)
                        if a1.name=='vn':
                            print('{}使出了六道阴阳遁手里剑，对方受到伤害'.format(a1.name))
                            print ("\n"*2)
                        if a1.name=='卡萨丁':
                            print('{}使出了别天神，对方受到伤害'.format(a1.name)) 
                            print ("\n"*2)                       
                            a.blood-=a1.attact*2
                            print('血量为{}'.format(a.blood))
                        if a.blood<=0:
                            
                            print('{}获胜'.format(self.aname))
                            break


                    else:
                        if a1.name=='压缩':
                            print('{}使出了神罗天征，对方受到伤害'.format(a1.name))
                            print ("\n"*2)
                        if a1.name=='塞拉斯':
                            print('{}使出了仙术·明神门，对方受到伤害'.format(a1.name))
                            print ("\n"*2)
                        if a1.name=='vn':
                            print('{}使出了大玉螺旋丸，对方受到伤害'.format(a1.name))
                            print ("\n"*2)
                        if a1.name=='卡萨丁':
                            print('{}使出了月读，对方受到伤害'.format(a1.name))
                            print ("\n"*2)                        
                        a.blood-=a1.attact
                        print('血量为{}'.format(a.blood))
                        if a.blood<=0:
                            
                            print('{}获胜'.format(self.bname))
                            break


            else:                
                if random.random()<=a.crit:
                    if a.name=='压缩':
                        print('{}使出了地爆天星，对方受到伤害'.format(a.name))
                        print ("\n"*2)
                    if a.name=='塞拉斯':
                        print('{}使出了真数火影千手，对方受到伤害'.format(a.name))
                        print ("\n"*2)
                    if a.name=='vn':
                        print('{}使出了六道阴阳遁手里剑，对方受到伤害'.format(a.name))
                        print ("\n"*2)
                    if a.name=='卡萨丁':
                        print('{}使出了别天神，对方受到伤害'.format(a.name))
                        print ("\n"*2)                     
                    a1.blood=a1.blood-a.attact*2
                    print('血量为{}'.format(a1.blood))
                    if a.blood<=0:
                        
                        print('{}获胜'.format(self.aname))
                        break


                else:
                    if a.name=='压缩':
                        print('{}使出了神罗天征，对方受到伤害'.format(a.name))
                        print ("\n"*2)
                    if a.name=='塞拉斯':
                        print('{}使出了仙术·明神门，对方受到伤害'.format(a.name))
                        print ("\n"*2)
                    if a.name=='vn':
                        print('{}使出了大玉螺旋丸，对方受到伤害'.format(a.name))
                        print ("\n"*2)
                    if a.name=='卡萨丁':
                        print('{}使出了月读，对方受到伤害'.format(a.name))
                        print ("\n"*2)                
                    a1.blood-=a.attact
                    print('血量为{}'.format(a1.blood))
                    if a1.blood<=0:
                        
                        print('{}获胜'.format(self.aname))
                        break


        while g==0:
            if num==1:
                print('第%s回合%s率先开啥攻击'%(num,a1.name))
                print('\n')
            else:
                print('第%s回合'%(num))
                print('\n')
            if random.random()<=a.miss:


                if a1.name=='压缩':
                    l=['地爆天星','神罗天征']
                    i=random.randint(0,1)
                    print('{}使出了{}'.format(a1.name,l[i]))
                if a1.name=='塞拉斯':
                    l1=['真数火影千手','仙术·明神门']
                    i1=random.randint(0,1)
                    print('{}使出了{}'.format(a1.name,l1[i1]))
                if a1.name=='vn':
                    l2=['六道阴阳遁手里剑','大玉螺旋丸']
                    i2=random.randint(0,1)
                    print('{}使出了{}'.format(a1.name,l2[i2]))
                if a1.name=='卡萨丁':
                    l3=['别天神','月读']
                    i3=random.randint(0,1)
                    print('{}使出了{}'.format(a1.name,l3[i3])) 



                if a.name=='压缩':
                    print('{}使出了须佐能乎挡住了攻击'.format(a.name))
                    print ("\n"*2)
                if a.name=='塞拉斯':
                    print('{}使出了五重罗生门挡住了攻击'.format(a.name))
                    print ("\n"*2)
                if a.name=='vn':
                    print('{}使出了尾兽查克拉外衣挡住了攻击'.format(a.name))
                    print ("\n"*2)
                if a.name=='卡萨丁':
                    print('{}使出了加具土命挡住了攻击'.format(a.name))
                    print ("\n"*2)


                a.blood=a.blood

                if random.random()<=a1.miss:
                    if a.name=='压缩':
                        l=['地爆天星','神罗天征']
                        i=random.randint(0,1)
                        print('{}使出了{}'.format(a.name,l[i]))
                    if a.name=='塞拉斯':
                        l1=['真数火影千手','仙术·明神门']
                        i1=random.randint(0,1)
                        print('{}使出了{}'.format(a.name,l1[i1]))
                    if a.name=='vn':
                        l2=['六道阴阳遁手里剑','大玉螺旋丸']
                        i2=random.randint(0,1)
                        print('{}使出了{}'.format(a.name,l2[i2]))
                    if a.name=='卡萨丁':
                        l3=['别天神','月读']
                        i3=random.randint(0,1)
                        print('{}使出了{}'.format(a.name,l3[i3])) 






                    if a1.name=='压缩':
                        print('{}使出了须佐能乎挡住了攻击'.format(a1.name))
                        print ("\n"*2)
                    if a1.name=='塞拉斯':
                        print('{}使出了五重罗生门挡住了攻击'.format(a1.name))
                        print ("\n"*2)
                    if a1.name=='vn':
                        print('{}使出了尾兽查克拉外衣挡住了攻击'.format(a1.name))
                        print ("\n"*2)
                    if a1.name=='卡萨丁':
                        print('{}使出了加具土命挡住了攻击'.format(a1.name))
                        print ("\n"*2)



                    a1.blood=a1.blood



                else:
                    if random.random()<=a.crit:
                        if a.name=='压缩':
                            print('{}使出了地爆天星，对方受到伤害'.format(a.name))
                            print ("\n"*2)
                        if a.name=='塞拉斯':
                            print('{}使出了真数火影千手，对方受到伤害'.format(a.name))
                            print ("\n"*2)
                        if a.name=='vn':
                            print('{}使出了六道阴阳遁手里剑，对方受到伤害'.format(a.name))
                            print ("\n"*2)
                        if a.name=='卡萨丁':
                            print('{}使出了别天神，对方受到伤害'.format(a.name))
                            print ("\n"*2)
                            
                        a1.blood=a.blood-a.attact*2
                        print('血量为{}'.format(a1.blood))
                        if a1.blood<=0:
                                    
                            print('{}获胜'.format(self.aname))
                            break


                    else:
                        if a.name=='压缩':
                            print('{}使出了神罗天征，对方受到伤害'.format(a.name))
                            print ("\n"*2)
                        if a.name=='塞拉斯':
                            print('{}使出了仙术·明神门，对方受到伤害'.format(a.name))
                            print ("\n"*2)
                        if a.name=='vn':
                            print('{}使出了大玉螺旋丸，对方受到伤害'.format(a.name))
                            print ("\n"*2)
                        if a.name=='卡萨丁':
                            print('{}使出了月读，对方受到伤害'.format(a.name))
                            print ("\n"*2)
                        a1.blood-=a.attact
                        print('血量为{}'.format(a1.blood))
                        if a1.blood<=0:
                                    
                            print('{}获胜'.format(self.aname))
                            break



            else:
                if random.random()<=a1.crit:
                    if a1.name=='压缩':
                        print('{}使出了地爆天星，对方受到伤害'.format(a1.name))
                        print ("\n"*2)
                    if a1.name=='塞拉斯':
                        print('{}使出了真数火影千手，对方受到伤害'.format(a1.name))
                        print ("\n"*2)
                    if a1.name=='vn':
                        print('{}使出了六道阴阳遁手里剑，对方受到伤害'.format(a1.name))
                        print ("\n"*2)
                    if a1.name=='卡萨丁':
                        print('{}使出了别天神，对方受到伤害'.format(a1.name))
                        print ("\n"*2) 
                    a.blood-=a1.attact*2
                    print('血量为{}'.format(a.blood))
                    if a.blood<=0:
                                
                        print('{}获胜'.format(self.bname))
                        break



                else:
                    if a1.name=='压缩':
                        print('{}使出了神罗天征，对方受到伤害'.format(a1.name))
                        print ("\n"*2)
                    if a1.name=='塞拉斯':
                        print('{}使出了仙术·明神门，对方受到伤害'.format(a1.name))
                        print ("\n"*2)
                    if a1.name=='vn':
                        print('{}使出了大玉螺旋丸，对方受到伤害'.format(a1.name))
                        print ("\n"*2)
                    if a1.name=='卡萨丁':
                        print('{}使出了月读，对方受到伤害'.format(a1.name))
                        print ("\n"*2)
                        a.blood-=a1.attact
                        print('血量为{}'.format(a.blood))
                    if a.blood<=0:
                                
                        print('{}获胜'.format(self.bname))
                        break                    
                                               



    
        
print('请你选着角色，a：压缩（暴击0.4，血量：200，攻击：30，闪避率：0.1）b:塞拉斯（暴击0.2，血量：250，攻击：20，闪避率：0.3）')
print('c:vn(暴击率:0.3,血量：180，攻击35，闪避率：0.4)d：卡萨丁(暴击率：0.2，血量：180，攻击力：30，闪避率0.5)')
w=input('请输入你选的角色对应的字母用:')
y=input('请输入你选的角色对应的字母用:')

if w=='a':
    c=input('请输入第一个选的你的名字：')
    a=Role('压缩',200,30,0.4,0.1)
if w=='b':
    c=input('请输入第一个选的你的名字：')
    a=Role('塞拉斯',250,20,0.2,0.3)

elif w=='c':
    c=input('请输入第一个选的你的名字：')
    a=Role('vn',180,35,0.3,0.4)
elif w=='d':
    c=input('请输入第一个选的你的名字：')
    a=Role('卡萨丁',180,30,0.2,0.5)




if y=='a':
    c1=input('请输入第二个选的你的名字：')
    a1=Role('压缩',200,30,0.4,0.1)
if y=='b':
    c1=input('请输入第二个选的你的名字：')
    a1=Role('塞拉斯',250,20,0.2,0.3)

elif y=='c':
    c1=input('请输入第二个选的你的名字：')
    a1=Role('vn',180,35,0.3,0.4)
elif y=='d':
    c1=input('请输入第二个选的你的名字：')
    a1=Role('卡萨丁',180,30,0.2,0.5)


a2=Game(c,c1)
a2.playGame()