# 5、	交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59]
# 要求，被置换的两个位置需要input输入。
li=[14,25,98,75,23,1,4,56,59]
exchange_num1,exchange_num2=map(int,input().split(' '))
li[exchange_num1],li[exchange_num2]=li[exchange_num2],li[exchange_num1]
print(li)