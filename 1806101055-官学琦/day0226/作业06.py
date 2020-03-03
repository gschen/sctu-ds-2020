'''
6.	（使用def函数完成）编写一个函数，输入n为偶数时，
调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
'''
#解法一
def sum_num(num):
    if num%2==0:
        if num==2:
            return 1/2
        else:
            return 1/(num)+sum_num(num-2)
    else:
        if num==1:
            return 1
        else:
            return 1/(num)+sum_num(num-2)
print(sum_num(6))

#解法二
def sum_num2(num):
    sums=0
    if num%2==0:
        for i in range(2,num+1,2):
            sums+=1/i
    else:
        for i in range(1,num+1,2):
            sums+=1/i
    return sums