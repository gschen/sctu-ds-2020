#4.（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

sum=0
for x in range(1,5):
    for y in range(1,5):
        if x!=y:
            continue
        else:
            for n in range(1,5):
                if n==x or n==y:
                    continue
                else:
                    print(str(x)+str(y)+str(n),end=' ')
                    sum=sum+1
print('')
print('总计有'+str(sum)+'个数')