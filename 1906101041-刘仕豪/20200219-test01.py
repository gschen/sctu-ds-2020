#1
wrong_list = [1,10,20,30,40,50]  #这些数不能运算
def jiecheng(n):   
    if n > 0:
        return n*jiecheng(n-1)
    if n == 0:
        return 1
    else:
        return False
