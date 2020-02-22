list1=[14,25,98,75,23,1,4,56,59]
n=int(input())
s=0
if n<len(list1):
    while n>0:
        s=s+list1[n-1]**2
        n-=1
print(s)