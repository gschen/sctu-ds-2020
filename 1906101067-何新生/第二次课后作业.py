#第一题
x = int(input("请输入一个数字:"))
def f(x):
    N = 3*x**4-9*x**2+x/2
    return N
print(f(x))

#第二题
x = int(input("请输入一个成绩："))
def cj(x):
    if x<60:
        return "D"
    elif x<80:
        return "C"
    elif x<90:
        return "B"
    else:
        return "A"
print(cj(x))

#第三题
list = (1,2,3,4,5,6,7)
def lb(list):
    X = list[::2]
    print(X)
print(lb(list))

#第四题
list = ['1','2','3','4']
for x in range(0,4):
    for y in range(0,4):
        for z in range(0,4):
            for c in range(0,4):
                if x!=y and x!=z and x!=c and y!=z and z!=c and y!=c:
                    print("{}{}{}{}".format(list[x],list[y],list[z],list[c]))

#第五题
x = int(input("请输入正整数x:"))
y = int(input("请输入正整数y:"))
z = int(input("请输入正整数z:"))
if x>y:
    x,y=y,x
if x>z:
    x,z=z,x
if y>z:
    y,z=z,y
print(x,y,z)
