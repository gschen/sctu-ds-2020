#5.	（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
x=int(input("输入一个整数"))
y=int(input("输入一个整数"))
z=int(input("输入一个整数"))
if x >= y and x >= z:
    if y >= z:
        print('xyz')
    else:
        print('xzy')
elif y >= z and y >= x:
    if z >= x:
        print('yzx')
    else:
        print("yxz")
elif z >= x and z >=y:
    if x >= y:
        print('zxy')
    else:
        print('zyx')
    


#方法二
x,y,z=map(int,input().split())#split分隔作用
list=[x,y,z]
list.sort()
print(list)