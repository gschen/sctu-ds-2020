left=["{","(","["]
right=["}",")","]"]

def check(string):
    ls=[]
    for i in string:
        if i in left:
            ls.append(i)
        if i in right:
            if len(ls)>0:
                left_key=ls.pop()
        
        right_index=right.index(i)
        left_index=left.index(left_key)

        if left_index!=right_index:
            return False
    if len(ls)==0:
        return True
    else:
        return False   