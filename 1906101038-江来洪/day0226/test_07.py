a,b,c,d = 0,0,0,0
str = input()
def jiang(str,a,b,c,d):
    for i in str:
        if i.isalpha():
            a += 1
        elif i.isdigit():
            b += 1
        elif i.isspace():
            c += 1
        else:
            d += 1
    return a,b,c,d
print(jiang(str,a,b,c,d))