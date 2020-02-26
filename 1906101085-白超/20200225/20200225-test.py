A={'a','b','c','c',1}
B={'a','a','b','b','c','c','e'}
print(A,B)

A={'a','b','c','c',1}
B={'a','a','b','b','c','c','e'}
print(A|B)

A={'a','b','c','c',1}
B={'a','a','b','b','c','c','e'}
print(A&B)

A={'a','b','c','c',1}
B={'a','a','b','b','c','c','e'}
print(A-B)

A={'a','b','c','c',1}
B={'a','a','b','b','c','c','e'}
print(B-A)

A={'a','b','c','c',1}
B={'a','a','b','b','c','c','e'}
print(A^B)

A={'a','b','c','c',1}
A.add('d')
print(A)

B={'a','a','b','b','c','c','e'}
B.update('e',[1,3])
print(B)



print(A,B)


print(B)

B={'a','a','b','b','c','c','e'}
B.pop()
print(B)

A={'a','b','c','c',1}
A.clear()
print(A)

dic={'name':'白超','age':18,'school':'CL'}
print(dic)

dic={'name':'白超','age':18,'school':'CL'}
dic['name']='panpan'
print(dic)

dic={'name':'白超','age':18,'school':'CL'}
dic.get('18')
print(dic)

dic={'name':'白超','age':18,'school':'CL'}
del dic['name']
print(dic)

dic={'name':'白超','age':18,'school':'CL'}
dic.pop('name')
print(dic)

dic={'name':'白超','age':18,'school':'CL'}
dic.popitem()
print(dic)