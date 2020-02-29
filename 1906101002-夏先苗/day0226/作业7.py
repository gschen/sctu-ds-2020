# （使用def函数完成）写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
# 样例输入
# D,a, ,s,1,3,2, ,a,2,d,a
# 样例输出
# 4, 6, 3, 0
def str_number(str_num):
    count=0
    count2=0
    count3=0
    count4=0
    for i in str_num:
        if i.isdigit()==True:
            count+=1
        elif i.isalpha()==True:
            count2+=1
        elif i.isspace()==True:
            count3+=1
        else:
            count4+=1
    print('数字有%d个'%count)
    print('字母有%d个'%count2)
    print('空格有%d个'%count3)
    print('其他有%d个'%count4)
num=input('输入：')
str_number(num)