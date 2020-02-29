def intro(p):
    li = []
    for i in range(len(p)):
        if i % 2 != 1:
            li.append(p[i])
    return li
list1 = input("请输入以以空格为间隔的整数:").split()
result = intro(list1)
print(result)
        



        
        
