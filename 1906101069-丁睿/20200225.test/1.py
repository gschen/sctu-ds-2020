A={"a","b","c","c",1}
B=set("aabbcce")
print(A|B)
print(A&B)
print(A-B)
print(A^B)
A.add("d")
B.update({1,3},{4,2},"e")
A.remove("a")
A.discard("f")
A.pop()

#字典
dic={"name":"张三","age":19,"school":"sctu"}
#修改数据
dic["name"]="李四"
dic.get("address")
dic.gesetdefault("name")
dic.setdefault("address","成都")
#增加数据
dic["class"]="1班"
#删除数据
del dic["name"]
dic.pop("name")
dic.popitem()