1

# def abc(x):
#     y = 3*(x**4) - 9*(x**2) + x/2
#     return y
# list=[54,96,83,64,234,158,364]
# for i in list:
#     print(abc(i),end = ' ')

2
# def grade(x:int):
    #     if x >= 90:
#         return 'A'
#     if x<90 and x>=80:
#         return 'B'
#     if x<80 and x>=60:
#         return 'C'
#     if x < 60:
#         return 'D'
# x = int(input('请输入成绩：'))
# print('成绩的等级：{}'.format(grade(x)))
3
# a = list(map(int,input("请输入列表：(并用,隔开)").split(',')))
# for i in a:
#     if i %2 == 0:
#        a.remove(i)
# print("列表奇数位组成新列表：{}".format(a))
4
# list = ['1','2','3','4']
# list1 = []
# for i in list:
#     for x in list:
#         for y in list:
#             a = i+x+y
#             if a not in  list1:
#                 list1.append(a)
# print("能组成{}个互不相同且无重复数字的三位数".format(len(list1)))
# for i in list1:
#     print(i,end = ' ')
5
#a = list(map(int,input("输入三个整数x,y,z(并用“,”隔开)：").split(',')))
# a.sort()
# for i in a:
#     print(i,end = ' ')
6
#def hhh(a):
#        s = 0
#     for i in range(2,a+1,2):
#         s += 1/i
#     return s
# def emm(a):
#     s = 0
#     for i in range(1,a+1,2):
#         s += 1/i
#     return s
# a = int(input("请输入一个整数："))
# if a%2 == 0:
#     print(hhh(a))
# else:
#     print(emm(a))
7
#s = input('请输入字符串：')
# a = []
# b = []
# c = []
# d = []
# for i in iter(s):
#     if i.isalpha():
#         a.append(i)
#     elif i.isdigit():
#         b.append(i)
#     elif i.isspace():
#         c.append(i)
# print("英文字符：{}个数：{},数字：{}个数:{},空格：{}个数：{},其它字符：{}个数：{}".format(len(a),len(b),len(c),len(d)))






