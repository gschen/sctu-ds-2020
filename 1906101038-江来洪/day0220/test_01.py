x = int(input())
wrong_nums = [1,10,20,30,40,50]
def jiang(x):
    if x == 0:
        return 1
    else:
        return x*jiang(x-1)
if x in wrong_nums:
    print('wrong num')
else:
    print(jiang(x)) 