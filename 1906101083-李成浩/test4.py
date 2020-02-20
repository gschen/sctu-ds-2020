l=[14,25,98,75,23,1,4,56,59]
n=int(input())
m=0
for i in l:
    if n>0:
        m+=i
        n-=1
    else:
        print(m)
        break