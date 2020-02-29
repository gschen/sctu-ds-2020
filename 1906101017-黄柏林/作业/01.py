# 所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。
limit=[1,10,20,30,40,50]
a=input('输入所求的数:')
a=int(a)
def jiecheng(a):
    if a==0:
        return 1
    else:
        return a*jiecheng(a-1)
print(jiecheng(3))
if a in limit:
    print('禁止运算')
else:
    print(jiecheng(a))

