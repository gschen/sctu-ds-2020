class Person():
    def _init_(self,name,blood,power,crit,avoid):
        self.name=name
        self.blood=blood
        self.power=power
        self.crit=crit
        self.avoid=avoid
    # 攻击
    def attack(self,object):
        # 对方是否闪避本次攻击
        # 表示我方命中
        if random.random >=object.avoid：
        # 判断是否暴击
        if random.random()<=self.crit:
            object.blood-=self.power*2
        else:
            object.blood-=self.power

class Game():
    def _init_(self,one,two):
        # 导入solo双方
        self.one=one
        self.two=two
    def solo(self):
        while True:
            one.attack(two)
            if two.blood<=0