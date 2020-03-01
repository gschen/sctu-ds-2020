a,b,c=map(int,input('请输入三个数(用空格隔开)：').split( ))
if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if b > c:
    b,c = c,b
print(a,b,c)