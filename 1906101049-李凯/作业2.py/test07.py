'''7.	（使用def函数完成）写函数，统计字符串中有几个字母，几个数字，
几个空格，几个其他字符，并返回结果
样例输入
D,a, ,s,1,3,2, ,a,2,d,a
样例输出
4, 6, 3, 0
'''
def list(n):
    letter=[]
    number=[]
    spare=[]
    other=[]
    for k in n:
        if k==' ':
            spare.append(k)
        elif k in range(0,10):
            number.append(k)
        elif k.isalpha():
            letter.append(k)
        else:
            other.append(k)
    return len(letter),len(number),len(spare),len(other)
print(list(['D','a',' ','s',1,3,2,' ','a',2,'d','a']))