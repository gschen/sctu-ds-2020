'''
5.	（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
'''
#解法一
a=int(input())
b=int(input())
c=int(input())
list=[]
if a>=b and a>=c :
    if b>=c:
        print('abc')
    else:
        print('acb')
elif b>=a and b>=c:
    if a>=c:
        print('bac') 
    else:
        print('bca')
elif c>=a and c>=b:
    if a>=b:
        print('cab')
    else:
        print('cba')   

#解法二
# x,y,z=map(int,input().split())
# ls=[x,y,z]
# ls.sort()
# print(ls)