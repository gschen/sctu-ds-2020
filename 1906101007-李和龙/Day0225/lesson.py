#构建

A = {"a","f","s","s","w"}
B = set("asdccs")
print(A,B)

#差(补)
print(A-B)

#并
print(A|B)

#交
print(A&B)

#不同时包含
print(A^B)

#增添
A.add("s")
print(A)


A.add("u")
print(A)

B.update({"p","o"},["r","y"],"t")
print(B)

#删除

A.remove("a")
print(A)
A.clear()
print(A)


print(B.pop())
print(B)




#zidian

dict1={"name:":"lihelong","age:":"19"}
print(dict1)


print(dict1.get("name"))

