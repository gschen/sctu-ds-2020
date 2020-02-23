#1
num = int(input("请输入一个数字: "))
a=1
if num < 0:
   print("抱歉，负数没有阶乘")
if num == 1 or num == 10 or num == 20 or num == 30 or num == 40 or num == 50 :
   print("抱歉，所求阶乘的数不可以是这几个数")
elif num == 0:
   print("0 的阶乘为 1")
else:
       for i in range(1,num + 1):
           a = a*i
       print("%d 的阶乘为 %d" %(num,a))


#2
P, T, R = eval(input("请依次输入P,T,R:"))
S = (P*T*R)/100
print(S)


#3
a = [14,25,98,75,23,1,4,56,59]
print('最大的元素为：', max(a))


#4
a = [14,25,98,75,23,1,4,56,59]
n = int(input("请输入一个数字n: "))
b = a[:n]
c = 0
if n < 0:
    print("抱歉，不符合题意")
elif n > 9:
    print("抱歉，不符合题意")
else:
    for i in b:
        c+=i**2
    print(c)


#5 
l = [14,25,98,75,23,1,4,56,59]
n,m = eval(input("请依次输入要交换的两个数："))
a = int(l.index(n))
b = int(l.index(m))          #这里的引号居然不能加，太坑了！！！
l[a], l[b] = l[b], l[a]
print(l)

