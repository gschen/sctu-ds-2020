#第五题
n1,n2=map(int,input().split(' '))
d=[14,25,98,75,23,1,4,56,59]
if n1>len(d) or n2>len(d):
    print('索引超出范围')
d[n1],d[n2]=d[n2],d[n1]
print(d)