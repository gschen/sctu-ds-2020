#NO.1
def f(x):
    return 3*x**4-9*x**2+x/2
print(f(54))

#NO.2
def f(x):
    if x<=100 and x>=90:
        return 'A'
    elif x>=80:
        return 'B'
    elif x >=60:
        return 'C'
    else:
        return 'D'
print(f(99))


#NO.3
def f(*s):
    return list(s)[::2]
print(f(1,2,3,4,5,6,7))



#NO.4
print([x+y for x in '1234' for y in '1234'])



#NO.5
x=int(input('数字:'))
y=int(input('数字:'))
z=int(input('数字:'))
if x>y:
    if y>z:
        return 'X>Y>Z'
    elif y<z:
        if x<z:
            return 'Z>X>Y'
        else:
            return 'X>Z>Y'
if z>y:
    if y>x:
        return 'Z>Y>X'
if y>x:
    if x>z:
        return 'Y>X>Z'
    else:
        if y>z:
            return 'Y>Z>X'
        else:
            return 'y>X>Z'




#NO.6
sum=0
s=0
def f(n):
    if n==0:
        return '请重新数入'
    if n%2==0:
        for x in range(1,x+1,2):
            s=s+1/x
        return s 
    else:
        for y in range(1,n+1,2):
            sum=sum+1/y
        return sum

print(f(2))


#NO.7

