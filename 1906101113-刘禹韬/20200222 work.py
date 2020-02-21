#1
x=int(input("输入要求阶乘的数"))
s=1
if x not in [1,10,20,30,40,50]:
    for i in range(1,x+1):
      s=s*i
    print(s)
else:
    print("所输入数不符合要求")



#2
P=input("输入本金")
T=input("输入时间")
R=input("输入利率")
D=(int(P)*int(T)*int(R))/100
print(D)


#3
list=[14,25,98,75,23,1,4,56,59]
list1=list
list1.sort()
print(list1[-1])


#4
n=int(input("希望求和的个数"))
list=[14,25,98,75,23,1,4,56,59]
list2=list[0:n]
h=0
for x in list2:
    h=h+x*x
print(h)


#5
a=int(input("输入要交换的两个元素"))
b=int(input())
list=[14,25,98,75,23,1,4,56,59]
a1=list.index(a)
b1=list.index(b)
list.pop(a1)
list.insert(a1,b)
list.pop(b1)
list.insert(b1,a)

