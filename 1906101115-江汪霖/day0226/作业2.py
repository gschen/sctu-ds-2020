n = int(input('请输入你的成绩：')) 
def cheng(a):
    if a < 101:
        if a >= 90:
            print('A')
        if a >= 80 and a < 90:
            print('B')
        if a >= 60 and a < 80:
            print('C')
        if a < 60:
            print('D')
cheng(n)