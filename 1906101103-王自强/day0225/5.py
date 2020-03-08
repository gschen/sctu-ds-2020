#5. 三个数排序（个数少）
A=list(map(int,input('依次输入x,y,z:').split(' ')))
for i in range(len(A)-1):
    if A[i]>A[i+1]:
        A[i],A[i+1]=A[i+1],A[i]
print(A)