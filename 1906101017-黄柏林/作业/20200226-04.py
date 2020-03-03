# 4.	（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
list=[1,2,3,4]
list1=[]
for a in list:
    for b in list:
        for c in list:
            if a!=b and a!=c and b!=c:
                list1.append(print(a,b,c))
print('循环次数:',len(list1))