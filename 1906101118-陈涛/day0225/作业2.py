#第一题
def f(x):
    a=(3*x**4)
    b=(9*x**2)
    c=x/2
    print(a-b+c)
f(54)
f(96)
f(83)
f(64)
f(234)
f(158)
f(364)

#第二题
def score(x):
    if x>=90:
        print('A')
    elif x>=80:
        print('B')
    elif x>=60:
        print('C')
    else:
        print('D')
score(60)

#第三题
def find_odd(a):
    i =a[0::2]
    print(i)
find_odd([1,2,3,4,5,6,7,8,9,11,111])

#第四题
a=0
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if (x!=y) and (y!=z) and (z!=x):
                a=a+1
                print(a,end="")
                print((x,y,z))

                

#第六题
def xuan(n):
    sum=0
    while n>0:
        if n %2 ==0:
            sum += 1/n
            n = n-2
        else:
            sum += 1/n
            n = n-2
    return sum
print(xuan(5))

#第七题
def find(a_number):
    number = 0
    grapheme = 0
    space = 0
    other = 0
    for i in a_number:
        if i.isalpha() == True:
            grapheme += 1
        elif i.isdigit() == True:
            number += 1
        elif i.isspace() == True:
            space += 1
        else:
            other += 1
    print("数字有%s个，字母有%s个，空格有%s个，其他字符有%s个"
     % (number,grapheme,space,other))
a_number = input('输入')
find(a_number)







