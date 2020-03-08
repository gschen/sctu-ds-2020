def n(a):
    zimu=0
    shuzi=0
    kongge=0
    qita=0
    for i in a:
        if i.isalpha():
            zimu+=1
        elif i.isdigit():
            shuzi+=1
        elif i.isspace():
            kongge+=1
        else:
            qita+=1
    print(zimu,shuzi,kongge,qita)
a=input('输入字符：')
print(n(a))



