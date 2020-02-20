#第一题
l=[1,10,20,30,40,50]
x=int(input())
if x not in l:
    def jc(i):
        if i==1:
            return 1
        return i*jc(i-1)
    print(jc(x))




#第二题
P=int(input('P='))
R=int(input('R='))
T=int(input('T='))
print('%d'% ((P*T*R)/100))



#第三题
l=[14,25,98,75,23,1,4,56,59]
print(max(l))



#第四题
l=[14,25,98,75,23,1,4,56,59]
n=int(input())
m=0
for i in l:
    if n>0:
        m+=i
        n-=1
    else:
        print(m)
        break



#第五题

l=[14,25,98,75,23,1,4,56,59]
m=int(input('位置一：'))-1
n=int(input('位置二：'))-1
a=l[m]
b=l[n]
l[m]=b
l[n]=a
print(l)