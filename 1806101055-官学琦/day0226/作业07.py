'''
7.	（使用def函数完成）写函数，
统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
'''
#解法一
def re_num(ls):
    res=[0]*4
    for i in ls:
        if type(i)==int:
            res[1]+=1
        elif 65<=ord(i)<=122:
            res[0]+=1
        elif ord(i)==32:
            res[2]+=1
        else:
            res[3]+=1
    return res
print(re_num(['D','a',' ','s',1,3,2,' ','a',2,'a','a']))

#解法二
def re_num2(ls):
    res=[0]*4
    for i in ls:
        if type(i)==int:
            res[1]+=1
        elif i.isalpha():
            res[0]+=1
        elif i==" ":
            res[2]+=1
        else:
            res[3]+=1
    return res
print(re_num(['D','a',' ','s',1,3,2,' ','a',2,'a','a']))