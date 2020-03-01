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
