"""
4、	求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
要求：n需要是input输入，且小于数组长度，不能固定。

"""

n = int(input())
list1 = [14,25,98,75,23,1,4,56,59]
list_result = []
lenth = len(list1)

if n > lenth:
    print("error")
else:
    for i in range(n):
        list_result.append(list1[i]**2)
    result = sum(list_result)
print(result)