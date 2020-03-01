#1
def f(x):
    return 3*4-9*2+x/2
print(f(54),f(96),f(83),f(64),f(234),f(158),f(364))

#2
def grade(n):
    if n<=100 and n >90:
        return 'A'
    elif n<=90 and n>80:
        return 'B'
    elif n<=80 and n>60:
        return 'C'
    else:
        return 'D'
print(grade(85))

#3
l1=[1,2,3,4,5,6,7]
print(l1[::2])

#4
l2=[]
for a in [1,2,3,4]:
    for b in [1, 2, 3, 4]:
        for c in [1, 2, 3, 4]:
            if a!=b and b!=c and c!=a:
                l2.append(a*100+b*10+c)
print(len(l2))
print(l2)

#5
x,y,z=map(int,input().split())
l=[x,y,z]
l.sort()
print(l)

#6
def num(n):
    s=0
    if n%2==0:
        for i in range(2,n+1,2):
            k=1/i
            s+=k
        return s
    else:
        for ii in range(1,n+1,2):
            kk=1/ii
            s+=kk
        return s
print(num(4))
print(num(5))

#7
def list(n):
    letter=[]
    number=[]
    spare=[]
    other=[]
    for k in n:
        if k==' ':
            spare.append(k)
        elif k in range(0,10):
            number.append(k)
        elif k.isalpha():
            letter.append(k)
        else:
            other.append(k)
    return len(letter),len(number),len(spare),len(other)
print(list(['D','a',' ','s',1,3,2,' ','a',2,'d','a']))