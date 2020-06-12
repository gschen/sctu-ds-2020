f = open('D:\111\meituan','r',encoding='utf-8')
w = open('D:\111meituan2','w',encoding='utf-8')
data = f.readlines()
for line in data:
    if line.split():
        w.writelines(line)
f.close()
w.close()
