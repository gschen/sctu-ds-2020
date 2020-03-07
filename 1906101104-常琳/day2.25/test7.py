#7.	（使用def函数完成）写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
#样例输入:D,a, ,s,1,3,2, ,a,2,d,a
#样例输出:4, 6, 3, 0

def f(strs):
    int_count,str_count,spa_count,other_count = 0,0,0,0
    for i in strs:
        if i.isdigit():
            int_count += 1
        elif i.isalnum():   
            str_count += 1
        elif i.isspace():   
            spa_count += 1
        else:
            other_count += 1
    print("字符串中，数字个数={}，字母个数={}，空格个数={}，其他个数={}".format(int_count,str_count,spa_count,other_count))
strs=input("请输入字符串：")
print(f(strs))


#用ASCII码来解决
def g(x):
    y=[0]*4
    for i in x:
        if type(i)==int:
            y[1]+=1
        elif 65<=ord(i)<=122:
            y[0]+=1
        elif i==' ':
            y[2]+=1
        else:
            y[3]+=1
    return y
print(g(['D','a','c',1,2,3,' ','@']))