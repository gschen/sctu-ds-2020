#7.	（使用def函数完成）写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
#样例输入：D,a, ,s,1,3,2, ,a,2,d,a  

def func(s):
    dic = {'数字':0,'字母':0,'空格':0,'其他字符':0}
    for i in s:
        if i.isdigit():
            dic['数字']+=1
        elif i.isalpha():
            dic['字母'] += 1
        elif i.isspace():
            dic['空格'] += 1
        else:
            dic['其他字符'] += 1
    return dic
print(func('D,a, ,s,1,3,2, ,a,2,d,a'))