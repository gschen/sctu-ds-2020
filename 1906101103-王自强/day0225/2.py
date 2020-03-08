#2. 等级
def dj(y):
    if y<=100 and y>=90:
        return 'A'
    elif y>=80:
        return 'B'
    elif y>=60:
        return 'C'
    else:
        return 'D'
print(dj(85))