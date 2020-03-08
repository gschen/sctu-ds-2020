# 7.	（使用def函数完成）写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
# 样例输入
# D,a, ,s,1,3,2, ,a,2,d,a
# 样例输出
# 4, 6, 2, 0
def judge(*x):
    num_1=0
    num_2=0
    num_3=0
    num_4=0
    for i in x[0]:
        if i.isalpha():
            num_1+=1
        elif i.isdigit():
            num_2+=1
        elif i==' ':
            num_3+=1
        else:
            num_4+=1
    return '字母：{},数字：{},空格：{},其他：{}'.format(num_1,num_2,num_3,num_4)
print(judge(input().split(',')))