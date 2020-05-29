ls=[]
def pre(root,ls):
    if not root:
        return 
    ls.append(root.val)
    pre(root.left,ls)
    pre(root.right,ls)
pre(root1,ls)
pre(root2,ls)
ls.sort()
return ls

