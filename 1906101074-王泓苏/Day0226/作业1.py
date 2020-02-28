#第一题
# def f(x):
#     return 3*4-9*2+x/2
# print(f(54),f(96),f(83),f(64),f(234),f(158),f(364))

#第二题
# n=int(input("请输入成绩："))
# def grade(n):
#     if n<=100 and n>90:
#         return 'A'
#     elif n<=90 and n>80:
#         return 'B'
#     elif n<=80 and n>60:
#         return 'C'
#     else:
#         return 'D'
# print(grade(n))

#第三题
# def whs(*x):
#     list1=[]
#     h=len(x)
#     for i in range(0,h,2):
#         list1.append(x[i])
#     print(list1)
# whs(1,2,3,4,5,6,7)

#第四题
# list2=[]
# L=[1,2,3,4]
# for a in L:
#     for b in L:
#         for c in L:
#             if a!=b and b!=c and c!=a:
#                 list2.append(a*100+b*10+c)
# print(len(list2))
# print(list2)

#第五题
# x,y,z=map(int,input("请输入三个整数：").split(','))
# if x>y:
#     x,y=y,x
# if x>z:
#     x,z=z,x
# if y>z:
#     y,z=z,y
# print(x,y,z)

#第六题
# n=int(input("请输入n:"))
# def num(n):
#     s=0
#     if n%2==0:
#         for i in range(2,n+1,2):
#             j=1/i
#             s+=j
#         return s
#     else:
#         for i2 in range(1,n+1,2):
#             j2=1/i2
#             s+=j2
#         return s
# print(num(n))

#第七题
def count_strs(strs):
    char_number,num_number,space_number,other_number=0,0,0,0
    for i in strs:
        if i.isalpha():
            char_number+=1
        elif i.isdigit():
            num_number+=1
        elif i==' ':
            space_number+=1
        else:
            other_number+=1
    print('字符串中有%d个字母,%d个数字,%d个空格,%d个其他字符' %(char_number,num_number,space_number,other_number))
count_strs('Da s132 a2da')
