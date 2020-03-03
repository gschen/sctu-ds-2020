'''
3.	（使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表
'''
#解法一
def re_ls(ls):
    num=0
    len_ls=len(ls)
    res=[]
    while num<len_ls:
        res.append(ls[num])
        num+=2
    return res

#解法二
def re_ls2(ls):
    return ls[::2]