#第三题
x=[14,25,98,75,23,1,4,56,59]
for i in range(len(x)-1):
    if x[i]>x[i+1]:
        x[i+1]=x[i]
print(x[i+1])