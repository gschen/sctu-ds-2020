def DJ(x):
    if x > 100:
        print('超出范围')
    else:
        if x > 90 and x <= 100:
            print('A')
        elif x > 80 and x <=90:
            print('B')
        elif x > 60 and x <=80:
            print('C')
        elif x <=60:
            print('D')
DJ(85)
