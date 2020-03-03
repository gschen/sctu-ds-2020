#第四题
S=[1,2,3,4]
H=[]
for i in S:
    q=100*i
    for b in S:
        w=10*b
        for c in S:
            e=c
m=q+w+e
if m not in H:
    H.append(m)
s=len(H)
print('能组成%d个互不相同且无重复数字的三位数' % s)
print(H)