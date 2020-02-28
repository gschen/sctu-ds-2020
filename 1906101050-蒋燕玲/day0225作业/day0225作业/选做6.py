#6.（使用def函数完成）编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n



# def f(n):
#     s=0
#     if n ==1:
#         return 1
#     if n%2== 0:
#         for i in (2,n+1):
#             s=s+ 1/i+1/(i-2)
#             n-=2
#             if n == 0 :
#                 break
#     return s
#     if n%2==1:
#         for i in (1,n+1):
#             s=s+ 1/i+1/(i-2)
#             n-=2
#             if n==0 :
#                 break
#     return s
# n = int (input("请输入："))
# print(f(n))