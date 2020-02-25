# # #集合
# # a={'1','2','5','8'}
# # b=set('34567')
# # '''
# # print(a|b)  #集和并集
# # print(a&b)  #集合交集
# # print(a-b)  #集合的补集
# # print(a^b)  #集合不同时包含

# # a.add('10')
# # b.update(['a','b'],'0')
# # print(a,b)

# # #删除集合元素
# # a.remove('1')
# # print(a)

# # b.discard('6')
# # print(b)

# # b.pop()
# # print(b)
# # '''
# # #字典
# # dic={'name':'liar','age':18,'home':'earth'}
# # #修改数据
# # '''
# # dic['name']='L-lijiao'
# #查找数据
# dic.get('family')
# dic.setdefault('family',family='lala')
# #增加数据
# dic['family']='haha'
# #删除数据
# del dic['family']
# dic.pop('home') # 必须赋值
# # '''
# # dic.popitem()  #无需赋值，随机删除最后
# # print(dic)  

# def AplusB(a,b):
#     return a+b
# result=AplusB(1,2)
# print(result)

# def mianji(r):
#     return 3.14*r*r
# keke=mianji(3)
# print(keke)
# #print(mianji(3))

# a=2
# def main():
#     b=3
#     print(a)
# main()
# print(b)

# circle=lambda r,pi:r**2*pi
# print(circle(3,3.14))


'''
#不可更改对象
def change(a):
    a=10
b=2
change(b)
print(b)
'''
# c=[1,2,3]
# def change(x):
#     x.append([1,2,3])
# change(c)
# print(c)


b='123'
