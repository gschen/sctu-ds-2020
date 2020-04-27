'''7、（使用def函数完成）写函数，统计字符串中有几个字母，几个数字，几个空格，
几个其他字符，并返回结果
样例输入
D,a, ,s,1,3,2, ,a,2,d,a
样例输出
4, 6, 3, 0'''

a,b,c,d = 0,0,0,0
str = input()
def jia(str,a,b,c,d):
    for i in str:
        if i.isalpha(): #检测字符串中是否只由字母组成
            a = a + 1
        elif i.isdigit(): #检测字符串中是否只由数字组成
            b = b + 1
        elif i.isspace(): #检测字符串中是否只包含空格
            c = c + 1
        else:
            d = d + 1
    return a,b,c,d
print(jia(str,a,b,c,d))
