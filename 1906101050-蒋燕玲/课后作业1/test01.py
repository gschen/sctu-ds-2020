#1、求给定数的阶乘
def jiecheng(n):
     if n == 0 or n ==1:
          return 1
     else:
          return n * jiecheng(n-1)
print(jiecheng(6))