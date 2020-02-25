#第一题
x = 1
y = int(input("请输入要计算的数:"))
for i in range(1, y + 1):
   x = x * i
print(x)

#第二题
P,T,R=map(int,input('请输入三个数并用逗号隔开：').split(','))
s=((P*T*R)/100)
print(s)

#第三题
L=[14,25,98,75,23,1,4,56,59]
M=max(L)
print(M)

#第四题
L=[14,25,98,75,23,1,4,56,59]
n=int(input('请指定前几位：'))
if n>len(L):
    print('超出范围')
else:
    L=L[:n]
    s=0
for i in L:
    s+=i**2
print(s)


#第五题
n1,n2=map(int,input('请输入两个用逗号隔开的数：').split(','))
S=[14,25,98,75,23,1,4,56,59]
if n1>len(S) or n2>len(S):
    print('超出范围')
S[n1],S[n2]=S[n2],S[n1]
print(S)