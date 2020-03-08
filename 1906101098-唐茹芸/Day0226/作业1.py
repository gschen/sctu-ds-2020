



list=[54,96,83,64,243,158,364]
def num(x):
    y=str(x)
    sum=0
    if x in list:
        g=3*y*y*y*y-9*y*y+y/2
        sum=sum+g
    return sum
print(sum)







def xx(a):
    a=input()
    if a>=90:
        print("A")
    elif 90>a>=80:
        print("B")
    elif 80>a>=60:
        print("C")
    elif 60>a:
        print("D")







def bb(arg):
    set=[]
    for i in range(len(arg)):
        if i % 2 == 1:
            set.append(arg[i])
        else:
            pass
    return set







num = 0
for i in range(1,5):
    for j in range (1,5):
        for k in range(1,5):
            if (i!=j) and (j!=k) and (k!=i):
                num+=1
                print(i,j,k)
print ("total num is :%d" %(num))







x=int(input('请输入x:'))
y=int(input('请输入y:'))
z=int(input('请输入z:'))
if x>y:
    x,y=y,x
if x>z:
    x,z=z,x 
if y>z:
    y,z=z,y
print(x,y,z)  







def aaa(x):
    x=[]
    str=input("请输入字符:")
    for i in str:
    x[i]=str.count(i)
print(x)




