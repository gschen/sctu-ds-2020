#set.intersection方法：即取交集
x = [1,2,3]
y = [3,4,5]
z = set(x).intersection(set(y))
s = set(x).intersection(y)
print(z)
print(s)

#collections中的deque类：deque类是python标准库collections模块中的一项
from collections import deque
d=deque()
d.append(3)
d.append(8)
d.append(1)
print(d)
s=deque('12345')
print(s)

d=deque(maxlen=20)
for i in range(30):
    d.append(i)
    print(d)

d=deque([1,2,3,4,5])
d.extend([0])
print(d)
d.extendleft([6,7,8])
print(d)

