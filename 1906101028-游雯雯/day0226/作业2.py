def cj(x):
    if 90 <= x <= 100:
        return 'A'
    elif 80 <= x < 90:
        return 'B'
    elif 60 <= x < 80:
        return 'C'
    else:
        return 'D'
x = int(input())
print(cj(x))