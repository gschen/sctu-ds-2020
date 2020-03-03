def f(n):
    a=b=c=d=0
    for i in n:
        if i.isalpha():
            a+=1
        elif i.isdigit():
            b+=1
        elif i.isspace():
            c+=1
        else:
            d+=1
    return a,b,c,d
print(f('Da s132 a2da'))