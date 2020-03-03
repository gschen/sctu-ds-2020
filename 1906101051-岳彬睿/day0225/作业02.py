#1
def f(x): 
    y = 3*x**4-9*x**2+x/2
    return y
print(list(map(f,[54,96,83,64,234,158,364])))

#2
def score(x):
    if 90 <= x <= 100:
        print('A')
    elif 80 <= x < 90:
        print('B')
    elif 60 <= x < 80:
        print('C')
    else:
        print('D')
print(score(x))

#3
list = (1,2,3,4,5,6,7)
def lb(list):
    X = list[::2]
    print(X)
print(lb(list))

#4
num=[1,2,3,4]
count = 0
for a in num:
    for b in num:
        for c in num:
            if a !=b and a!=c and b!=c:
                count +=1
                print('{},{},{}'.format(a,b,c))
print("一共有%d个"%count)

#5
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
