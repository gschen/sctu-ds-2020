A=list(map(int,input()))
m=int(input())
B=list(map(int,input()))
n=int(input())
for i in A:
    list1=[]
    if i==0:
        pass
    else:
        list1.append(i)
print(list1)
s=list1.extend(B)
print(s)