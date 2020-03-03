# #1
# def f(x):
#     y = 3*(x**4) - 9*(x**2) + x/2
#     return y
# lis = [54,96,83,64,234,158,364]
# for i in lis:
#     print(f(i),end = '      ')

# #2
# def grade(x:int):
#     if x >= 90:
#         return 'A'
#     if 90 > x >= 80:
#         return 'B'
#     if 80 >x>= 60:
#         return 'C'
#     if x < 60:
#         return 'D'
# x = int(input())
# print(grade(x))

# #3
# lis = list(map(int,input().split(',')))
# for i in lis:
#     if i %2 == 0:
#         lis.remove(i)
# print(lis)

# #4
# lis = ['1','2','3','4']
# l = []
# for i in lis:
#     for j in lis:
#         for k in lis:
#             a = i+j+k
#             if a not in  l:
#                 l.append(a)
# print(len(l))
# for i in l:
#     print(i,end = '  ')


# #5
# l = list(map(int,input().split(',')))
# l.sort()
# for i in l:
#     print(i,end = '  ')

# #6
# def ou(n):
#     s = 0
#     for i in range(2,n+1,2):
#         s += 1/i
#     return s
# def ji(n):
#     s = 0
#     for i in range(1,n+1,2):
#         s += 1/i
#     return s
# n = int(input())
# if n%2 == 0:
#     print(ou(n))
# else:
#     print(ji(n))

# #7
# s = input('请输入一行字符串：')
# 英文字符 = []
# 数字 = []
# 空格 = []
# 其它字符 = []
# for i in iter(s):
#     if i.isalpha():
#         英文字符.append(i)
#     elif i.isdigit():
#         数字.append(i)
#     elif i.isspace()
#         空格.append(i)
# print('''英文字符：{}个数：{}，数字：{}个数:{},空格：{}个数：{}，其它字符：{}个数：{}'''/.format(英文字符，len（英文字符），数字,len（数字)，空格，len(空格)，其它字符，len(其它字符)))

