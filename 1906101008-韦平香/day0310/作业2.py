#创建一个角色类(类)，包含属性有：角色名称、角色血量、攻击力、暴击率、闪避率。

class Role():
    def __init__(self,name,life_value,fight,crit,dodge):
        self.name = name
        self.life_value = life_value
        self.fight = fight
        self.crit = crit
        self.dodge = dodge

    def get_name(self):
        print(self.name)

    def get_life_value(self):
        print(self.life_value)

    def get_fight(self):
        print(self.fight)

    def get_crit(self):
        print(self.crit)

    def get_dodge(self):
        print(self.dodge)


b = Role('秦驰',100,1000,50,30)
b.get_name()
b.get_life_value()
b.get_fight()
b.get_crit()
b.get_dodge()