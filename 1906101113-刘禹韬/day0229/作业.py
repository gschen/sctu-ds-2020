#1
def f(x):
    h=3*x**4-9*x**2+x/2
    return h

l=[54,96,83,64,234,158,364]
for i in l:
    print(f(i))


#2
x=int(input("输入成绩"))
def point(x):
    if x < 60:
        return("D")
    elif x < 80:
        return("C")
    elif x < 90:
        return("B")
    else:
        return("A")
print(point(x))


#3
def jishu(x):
    l1=[]
    n=range(1,len(x)+1)
    for i in n:
        if i % 2==1:
            l1.append(x[i-1])
        else:
            pass
    return(l1)
    
l2=[1,2,3,4,5,6,7]
print(jishu(x))
    
    
#4
l3=[1,2,3,4]
m=0
for i in l3:
    for n in l3:
        for x in l3:
            if i!=n and i!=x and n!=x:
                m+=1
                print(i*100+n*10+x)
            else:
                pass


#5
l4=[]
for i in range(3):
    x=int(input("请输入整数"))
    l4.append(x)
l4.sort()
for x in l4:
    print(x)
        


