def G(x):
    if x>100:
        print('无效分数')
    elif 90<x<=100:
        print('A')
    elif 80<x<=90:
        print('B')
    elif 60<x<=80:
        print('C')
    else:
        print('D')

G(85)