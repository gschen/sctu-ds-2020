#请写一个函数，利用切片实现对字符串的首尾空格删除，不能使用str的strip()函数。请拍照纸质答案写上姓名上传图片。
def detel(i):
    while i[0]==' ':
        i=i[1:]
    while i[-1]==' ':
        i=i[:-1]
    return i
n=('   huangbolin   ')
print(detel(n))