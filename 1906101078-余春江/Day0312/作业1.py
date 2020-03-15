import random
class nature():
    def __init__(self,name,blood,attact,crit,miss):
        self.name=name
        self.blood=blood
        self.attact=attact
        self.crit=crit
        self.miss=miss


class Game():
    def __init__(self,aname,bname):
        self.aname=aname
        self.bname=bname

    def playgame(self):
        c=random.randint(0,1)
        num=1
        while c==1:
            if num==1:
                print('第%s局，%s得到先手'%(num,a.name))
                print('\n')
            num=num+1
            if random.random()<=a1.miss:
                a1.blood=a1.blood



                if a.name=='鸣人':
                    L=['风遁，螺旋手里剑','尾兽玉','仙法，超大玉螺旋丸']
                    i=random.randint(0,2)
                    print('{}发动{}'.format(a.name,L[i]))
                if a.name=='佐助':
                    L1=['火遁，豪火球之术','炎遁，加具土命','天照']
                    i1=random.randint(0,2)
                    print('{}发动{}'.format(a.name,L1[i1]))

                if a1.name=='鸣人':
                    print('{}开启了仙人模式，免疫此次伤害'.format(a1.name))
                    print('\n')
                if a1.name=="佐助":
                    print('{}开启了须佐能乎，免疫此次伤害'.format(a1.name))

                if random.random()<=a.miss:

                    if a.name == '鸣人':
                        L = ['风遁，螺旋手里剑', '尾兽玉', '仙法，超大玉螺旋丸']
                        i = random.randint(0, 2)
                        print('{}发动{}'.format(a.name, L[i]))
                    if a.name == '佐助':
                        L1 = ['火遁，豪火球之术', '炎遁，加具土命', '天照']
                        i1 = random.randint(0, 2)
                        print('{}发动{}'.format(a.name, L1[i1]))

                    if a1.name == '鸣人':
                        print('{}开启了仙人模式，免疫此次伤害'.format(a1.name))
                        print('\n')
                    if a1.name == "佐助":
                        print('{}开启了须佐能乎，免疫此次伤害'.format(a1.name))

                    else:
                        if random.random()<=a.crit:
                            if a.name == '鸣人':
                                print('{}使出风遁，螺旋手里剑，对方受到伤害'.format(a.name))
                                print("\n" * 2)
                            if a.name == '佐助':
                                print('{}使出了火遁，豪火球之术，对方受到伤害'.format(a.name))
                                print("\n" * 2)
                            a1.blood=a.blood-a.attact*2
                            print('血量为{}'.format(a1.blood))
                            if a1.blood<=0:

                                print('{}获得胜利'.format(self.aname))
                                break

                            else:
                                if random.random()<=a.crit:
                                    if a.name == '鸣人':
                                        print('{}使出风遁，螺旋手里剑，对方受到伤害'.format(a.name))
                                        print("\n" * 2)
                                    if a.name == '佐助':
                                        print('{}使出了火遁，豪火球之术，对方受到伤害'.format(a.name))
                                        print("\n" * 2)
                                    a1.blood=a.blood-a.attact*2
                                    print('血量为{}'.format(a1.blood))
                                    if a1.blood<=0:

                                        print('{}获得胜利'.format(self.aname))
                                        break

                                else:
                                    if random.random() <= a.crit:
                                        if a.name == '鸣人':
                                            print('{}使出风遁，螺旋手里剑，对方受到伤害'.format(a.name))
                                            print("\n" * 2)
                                        if a.name == '佐助':
                                            print('{}使出了火遁，豪火球之术，对方受到伤害'.format(a.name))
                                            print("\n" * 2)
                                        a1.blood = a.blood - a.attact * 2
                                        print('血量为{}'.format(a1.blood))
                                        if a1.blood <= 0:
                                            print('{}获得胜利'.format(self.aname))
                                            break



print('请选择角色，a:鸣人(暴击:0.5，血量：150，攻击：40，闪避率：0.1)b:佐助(暴击:0.6,血量：140，攻击：35，闪避率：0.11)')
m=input('请输入你选择的角色对应字母：')
y=input('请输入你选择的角色对应字母：')


if m=="a":
    c = input('请输入第一个选的你的名字：')
    a=nature("鸣人",200,40,0.5,0.1)
else:
    c = input('请输入第一个选的你的名字：')
    a=nature("佐助",140,35,0.6,0.11)

if y=="a":
    d = input('请输入第二个选的你的名字：')
    b=nature("鸣人",200,40,0.5,0.1)
else:
    d = input('请输入第二个选的你的名字：')
    b=nature("佐助",140,35,0.6,0.11)

a2=Game(c,d)
a2.playgame()