



a='hi'



b='s'



print(a+b)







#重复字符



c='hi'



print(c*3)







str1='abcde'



print(str1[0])



print(str1[-1])



print(str1[0:4])



print(str1[::-1])







print('b' in str1)



print('v' not in str1)







#格式化输出



print('我叫%s'%('ST-one'))



print('我叫{}'.format('ST-one'))



print('我今年%d'%(20))



print('我今年{}'.format(20))







#列表



list1=[1,2,3,[4,5,6]]



print(len(list1))







for x in [1,2,3]:



    print(x,end=' ')



print('')







list1.append(7)



print(list1)



list1.extend([1,2])



print(list1)



print(list1.index(2))



list1.pop(1)



print(list1)







list2=[5,8,6,4,2,5,8,9,1]



list2.sort()



print(list2)



# sorted有返回值，sort没有返回值







#元组



tup=('s',100,[1,2])



# tup[1]=200  元组元素不能被更改



print(tup)