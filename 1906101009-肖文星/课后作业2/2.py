def xwx(a):
    if 90<=a<=100:
        return 'A'
    elif 80<=a<90:
        return 'B'
    elif 60<=a<80:
        return 'C'
    elif 0<=a<60:
        return 'D'
    else:
        return '成绩不对'
print(xwx(100))