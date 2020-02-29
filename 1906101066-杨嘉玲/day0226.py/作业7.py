def opt(s):   
    char, num, space, other = 0, 0, 0, 0
    for i in s:
        if i.isalpha():
            char += 1
        elif i.isdigit():
            num += 1
        elif i == ' ':
            space += 1
        else:
            other += 1
    return char,num,space,other

s = input("请输入字符：")
result = opt(s)
char = result[0]
num = result[1]
space = result[2]
other = result[3]
print("该字符串中有字母：%d 个"%char)
print("该字符串中有数字：%d 个"%num)
print("该字符串中有空格：%d 个"%space)
print("该字符串中有其他：%d 个"%other)


