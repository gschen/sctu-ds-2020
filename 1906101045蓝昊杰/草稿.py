import math
array=[[1.0,2.0],[1.5,0.1], [1.8,1.4], [2.3,3.5]]
clas=['A','A','B','B']
text=[1,0.3]
lis=[]
k=3


#欧氏距离
def oushi(s):
    answer=0
    for i in array:
        for j in range(len(text)):
            answer+=(i[j]-text[j])**2
        lis.append((answer**(1/2)))
#曼哈顿距离
def manhadun(s):
    answer=0
    for i in array:
        for j in range(len(text)):
            answer+=abs((i[j]-text[j]))
        lis.append(answer)

#计算
def jisuan():
    l=""
    a=0
    b=0
    ls=sorted(lis)
    #获取A B的数量
    for n in range(k):
        ind=lis.index(ls[n])
        l+=clas[ind]
    #类别出现次数
    for m in l:
        if m=="A":
            a+=1
        else:
            b+=1
    if a>b:
        return "A"
    else:
        return "B"
# oushi(array)
manhadun(array)
print(jisuan())