score=eval(input('请输入成绩:'))
def chengji():
    if score>=90:
        print('A')
    if score>=80 and score<90:
        print('B')
    elif score>=60 and score<80:
        print('C')
    else:
        print('D')
chengji()