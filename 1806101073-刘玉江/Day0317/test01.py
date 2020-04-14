str1="((({{}}[]]{{}})))"
def kuohaopipei(str1):
    ls = []
    i = 0
    while i < len(str1):
        if str1[i] == "(" or str1[i] == "{" or str1[i]=="[":
            ls.append(str1[i])
            i+=1
            continue
        elif len(ls) == 0:
            return False
        a = ls.pop()
        if (str1[i] == ")" and a=="(") or (str1[i] == "}" and a=="{") or (str1[i] == "]" and a=="["):
            i+=1
        else:
            i+=1
    if len(ls) != 0 :
        return False
    return True
print(kuohaopipei(str1))