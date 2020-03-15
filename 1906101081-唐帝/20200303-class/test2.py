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

#。。