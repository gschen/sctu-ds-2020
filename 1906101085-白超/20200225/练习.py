L=[1,2,3,2]
a=L[0]
for i in L:
    if i >a:
        a=i
print(a)

#l=[1,2,3,'a',1]
#sum=0
#for i in l:
    #if isinstance(i,int):
    #sum=sum+i
#print(sum)

x=6
for i in range(2,x):
    if x % i == 0:
        print("不是素数")
        break
else:
    print("是")


