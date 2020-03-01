#1
def f(x):
    for i in x:
        s = 3*i**4-9*i**2+i/2
        print(s)
f(54,96,83,64,234,158,364)


#2
def f(n):
    if n >= 90 and n <= 100:
        return 'A'
    elif n >= 80:
        return 'B'
    elif n >= 60:
        return 'C'
    else:
        return 'D'


#3
def f(x):
    l1 = []
    for i in  range (len(x)):
        if i % 2 == 1:
            l1.append(x[i])
    return l1
print(f([1,2,3,4,5,6,7,8,9]))

#4
sum=0
for i in range(1,5):
    for j in range(1,5):
        if i==j:
            continue
        else:
            for l in range(1,5):
                if l==i or l==j:
                    continue
                else:
                    print(str(i)+str(j)+str(l),end=' ')
                    sum=sum+1
print('')
print('总计有'+str(sum)+'个数')

#5
num = []
for i in range(4):
    if i > 0:
        x = int(input())
        num.append(x)
print(sorted(num))


#6
def main(n):
    sum=0
    if n%2==0:
        for i in range(2,n+1,2):
            a=1/i
            sum += a
        print(sum)
    else:
        for i in range(1,n+1,2):
            a=1/i
            sum += a
        print(sum)
n=int(input('请输入一个数:'))
main(n)


#7
def f(m):
    a = b = c = d = 0
    for i in m:
        if i.isalpha():
            a += 1
        elif i.isdigit():
            b += 1
        elif i.isspace():
            c += 1
        else:
            d += 1
    return a,b,c,d
print(f('Da s132 a2da'))
