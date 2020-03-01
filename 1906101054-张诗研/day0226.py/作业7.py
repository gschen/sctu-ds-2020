#7.（使用def函数完成）写函数，
#统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
s=input('输入一行字符:\n')
i=0
j=0
k=0
l=0
for c in s:
    if c.isalpha():
        i+=1
    elif c.isspace():
       j+=1
    elif c.isdigit():
        k+=1
    else:
        l+=1
print('英文=%d,空格=%d,数字=%d,其他字符=%d'%(i,j,k,l))