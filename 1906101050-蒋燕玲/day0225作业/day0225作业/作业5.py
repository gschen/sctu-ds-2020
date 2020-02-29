#5.（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
x,y,z=map(int,input("请输入：").split())
l=[x,y,z]
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[j],l[i]=l[i],l[j]
print(l)