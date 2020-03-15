class Gameperson():
    def __init__(self,name,blood,aggressivity,violence,dodge):
        self.name = name
        self.blood = blood
        self.aggressivity = aggressivity
        self.violence = violence
        self.dodge = dodge
    def information(self):
        print('玩家名称：%s\n血量：%s\n攻击力：%s\n暴击率：%s\n闪避率：%s' % (self.name,self.blood,self.aggressivity,self.violence,self.dodge))
a = Gameperson('八里公路',5000,1000,0.5,0.5)
b = Gameperson('大魔王',10000,500,0.2,0.2)
a.information()
b.information()