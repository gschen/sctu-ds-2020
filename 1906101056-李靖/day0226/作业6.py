#6
n = int(input('请输入：'))				
def jiou(x):
    if x == 1:
       return 1/1
    elif x == 2:
       return 1/2
    else:
       return 1/x+jiou(x-2)
print(jiou(n))
