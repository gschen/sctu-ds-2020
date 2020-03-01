def dengji(kw):
    if kw>=90 and kw<=100:
        return ('等级为A')
    if kw<90 and kw>=80:
        return ('等级为B')
    elif kw<80 and kw>=60:
        return ('等级为C')
    else:
        return('等级为D')
a=eval(input('请输入你的成绩：'))
print(dengji(a))