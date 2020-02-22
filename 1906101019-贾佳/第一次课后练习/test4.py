n = int(input("num"))
l = [14,25,98,75,23,1,4,56,59]
if n>9 or n<1:
    print("超出范围")
else:
    s = l[0:n]
    print([x*x for x in s])