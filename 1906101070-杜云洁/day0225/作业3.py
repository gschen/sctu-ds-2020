#3.（使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表
# def hi(x):
#     s=[ ]
#     for i in range(len(x)):
#         if i%2==0:
#             s.append(x[i])
#         else:
#             pass
#     return s
# nums=[1,2,3,4,5,6,7]
# r=hi(nums)
# print(nums)
# print(r)

#方法二
def re_list(list1):
    return list1[::2]
list1=[1,2,3,4,5,6,7]
print(list1)