#用递归求n的阶乘

def Li(num):
    if num > 1:
        return num * Li(num - 1)
    else:
        return num
 
print(Li(6))