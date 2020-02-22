#3、	查找数组中的最大元素:[14,25,98,75,23,1,4,56,59]。

list = [14,25,98,75,23,1,4,56,59]
max = list[0]
for i in range(1, len(list)):
    if max < list[i]:
        max = list[i]
print(max)