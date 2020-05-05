ls=[]
def pre(root):#前序
    if not root:
        return
    ls.append(root.val)
    pre(root.left,ls)
    pre(root.right,ls)
def mid(root,ls):
    if not root:
        return
    mid(root.left,ls)
    ls.append(root.val)
    mid(root.right,ls)
def back(root,ls):
    if not root:
        return
    back(root.left,ls)
    
    back(root.right,ls)
    ls.append(root.val)

