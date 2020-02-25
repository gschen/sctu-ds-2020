"""
list=[1,2,3,4]
a=list[0]
for i in list:
    if i>a:
        a=i
print(a)

list=[1,2,3,4,'a']
sum=0
for i in list:
    if isinstance(i,int):
        sum+=i
print(sum)
"""
x=5
for i in range(2,x):
    if x%i==0:
        print("不是")
        break
else:
    print("是")
#判断是不是素数