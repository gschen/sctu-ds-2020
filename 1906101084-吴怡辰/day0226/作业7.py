def tongji(l):
    alpha=0;digit=0;space=0;others=0
    for i in l:
        if i.isalpha():
            alpha += 1
        elif i.isdigit():
            digit += 1
        elif i.isspace():
            space += 1
        else:
            others += 1
    print(alpha,digit,space,others)
l = list(map(str,input().split(',')))
tongji(l)


# ACSII码
# def res(l):
#     res = [0]*4
#     for i in l:
#         if 65 <= ord(i) <=90 or 97 <= ord(i) <= 122:
#             res[0] += +1
#         elif type(i) == int:
#             res[2] += 1
#         elif ord(i) == 32:
#             res[3] += 1
#     return res
# l = list(map(str,input().split(',')))
# print(res(l))
