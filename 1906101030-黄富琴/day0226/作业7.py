n=input('请输入字符串:')
a=b=c=d=0
for i in n:
    if i.isalpha():
        a+=1
    elif i =='':
        b+=1
    elif i.isdigit():
        c+=1
    else:
        d+=1
print('字母为{},数字为{},空格为{},其他为{}'.format(a,b,c,d))

