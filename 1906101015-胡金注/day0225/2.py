def f(x):
    if 90<= x <=100:
        return 'A'
    elif 80<= x <90:
        return 'B'
    elif 60<= x <80:
        return 'C'
    elif x <60:
        return 'D'
print(f(int(input())))
