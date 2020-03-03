'''
第一题
def f(x):
    return 3*(x**4)-9*(x**2)+(x/2)

第二题
def grade(num):
    if 90<num<=100:
        return A
    elif 80<num<=90:
        return B
    elif 60<num<=80:
        return C
    elif 0<=num<=60:
        return D

第三题
解法一
def re_ls(ls):
    num=0
    len_ls=len(ls)
    res=[]
    while num<len_ls:
        res.append(ls[num])
        num+=2
    return res

解法二
def re_ls(ls):
    return ls[::2]

第四题
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a!=b and a!=c and c!=b:
                print('{}{}{}'.format(a,b,c))

第五题
a=int(input())
b=int(input())
c=int(input())
list=[]
if a>=b and a>=c :
    if b>=c:
        print('abc')
    else:
        print('acb')
elif b>=a and b>=c:
    if a>=c:
        print('bac') 
    else:
        print('bca')
elif c>=a and c>=b:
    if a>=b:
        print('cab')
    else:
        print('cba')   

解法二
x,y,z=map(int,input().split())
ls=[x,y,z]
ls.sort()
print(ls)

第六题
解法一
def sum_num(num):
    if num%2==0:
        if num==2:
            return 1/2
        else:
            return 1/(num)+sum_num(num-2)
    else:
        if num==1:
            return 1
        else:
            return 1/(num)+sum_num(num-2)
print(sum_num(6))

解法二
def sum_num(num):
    sums=0
    if num%2==0:
        for i in range(2,num+1,2):
            sums+=1/i
    else:
        for i in range(1,num+1,2):
            sums+=1/i
    return sums

第七题
def re_num(ls):
    res=[0]*4
    for i in ls:
        if type(i)==int:
            res[1]+=1
        elif 65<=ord(i)<=122:
            res[0]+=1
        elif ord(i)==32:
            res[2]+=1
        else:
            res[3]+=1
    return res
print(re_num(['D','a',' ','s',1,3,2,' ','a',2,'a','a']))

解法二
def re_num(ls):
    res=[0]*4
    for i in ls:
        if type(i)==int:
            res[1]+=1
        elif i.isalpha():
            res[0]+=1
        elif i==" ":
            res[2]+=1
        else:
            res[3]+=1
    return res
print(re_num(['D','a',' ','s',1,3,2,' ','a',2,'a','a']))
'''
