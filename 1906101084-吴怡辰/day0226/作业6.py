def dy(x):
    if x == 1:
       return 1/1
    elif x == 2:
       return 1/2
    else:
       return 1/x+dy(x-2)
n = int(input())
print(dy(n))

# def res(n):
#    sum = 0
#    if n % 2 == 0:
#       for i in range(2,n+1,2):
#          sum = sum + 1/i
#       return sum
#    else:
#       for  i in range(1,n+1,2):
#          sum = sum + 1/i
#       return sum
# print(res(6))



# n = int(input())
# def dy(x):
#     if x % 2 == 0:
#         a = 0
#         s = 0
#         for i in range(0,x):
#                 a += 2
#                 s += 1/a
#     else:
#         a = -1
#         s = 0
#         for j in range(0,x):
#                 a += 2
#                 s += 1/a
#     return s
# print(dy(n))
