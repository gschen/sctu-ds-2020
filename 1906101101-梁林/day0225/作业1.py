#1. 求解
def qj(x):
    return 3*x**4-9*x**2+x/2
print(qj(54))

#2. 等级
def dj(y):
    if y<=100 and y>=90:
        return 'A'
    elif y>=80:
        return 'B'
    elif y>=60:
        return 'C'
    else:
        return 'D'
print(dj(85))

#3. 奇数位
def js(*s):
    return list(s)[::2]
print(js(1,2,3,4,5,6,7))

#4. 重组
a=[1,2,3,4]
n=0
for i in a:
    for ii in a:
        for iii in a:
            if len(set([i,ii,iii]))==3:
                n+=1
print(n)

#5. 三个数排序（个数少）
A=list(map(int,input('依次输入x,y,z:').split(' ')))
for i in range(len(A)-1):
    if A[i]>A[i+1]:
        A[i],A[i+1]=A[i+1],A[i]
print(A)

#6. 数列
def sl(n):
    if n==0:
        return '重新输入'
    else:
        s=0
        if n%2==0:
            for i in range(2,n+1,2):
                s+=1/i
            return s
        else:
            for i in range(1,n+1,2):
                s+=1/i
            return s
        
print(sl(3))

#7. 统计
def tj(x):
    z,s,k,q=0,0,0,0
    for i in x:
        if i in list(map(chr,list(range(97,123)))) or i in list(map(chr,list(range(65,91)))):
            z+=1
        elif i in list(map(str,list(range(10)))):
            s+=1
        elif i==' ':
            k+=1
        else:
            q+=1
    return z,s,k,q
         
x='D,a, ,s,1,3,2, ,a,2,d,a, '.split(',')
print(x)
print(tj(x))




