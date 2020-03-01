def cj():
    x=int(input("请放入一个一百以内的数:"))
    if x >100:
        print("error")
    elif x >=90:
        print("A")
    elif x >=80:
        print("B")
    elif x >=60:
        print("C")
    else:
        print('D')
cj()