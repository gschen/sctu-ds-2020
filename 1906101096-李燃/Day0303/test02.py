class Test():
    def original(self):
        lis = [chr(i) for i in range(97,123)]    #chr():数字转换成字母（97-122是ACSII码对应小写字母a-z）
        print(lis)
        print(''.join(lis))    #  ''.join(lis）：把lis里的字母变成字符串的形式
    def overturn(self):
        li = (chr(i) for i in range(90,64,-1))   #65-90是ACSII码对应大写字母A-Z
        print(''.join(li))  
a = Test()
a.original()
a.overturn()
