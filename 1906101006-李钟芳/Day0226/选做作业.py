#6.（使用def函数完成）编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

def li(n,sum):
    sum += 1/n
    if n == 2 or n == 1:
        return sum
    else:
        return li(n-2,sum)
sum = 0
n = int(input())
print(li(n,sum))

# 7.（使用def函数完成）写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
# 样例输入
# D,a, ,s,1,3,2, ,a,2,d,a
# 样例输出
# 4, 6, 3, 0


# a,b,c,d = 0,0,0,0
# str = input()
# def li(str,a,b,c,d):
#     for i in str:
#         if i.isalpha():
#             a += 1
#         elif i.isdigit():
#             b += 1
#         elif i.isspace():
#             c += 1
#         else:
#             d += 1
#     return a,b,c,d
# print(li(str,a,b,c,d))
