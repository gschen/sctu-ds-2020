class Student:
    def __init__(get,name,age,course):
        get.name=name
        get.age=age
        get.course=course
    def get_name(get):
        print('我叫%s' % (get.name))
    def get_age(get):
        print('年龄为：%s' % (get.age))
    def get_course(get):
        print('三门课中最高分为：%s' % (max(get.course)))
tangdi=Student('唐帝',19,[100,90,80])
tangdi.get_name()
tangdi.get_age()
tangdi.get_course()