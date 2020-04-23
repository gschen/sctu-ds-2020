ls=[]
def pre(root,ls):
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

def pos(root,ls):
    if not root:
        return
    pos(root.left,ls)
    pos(root.right,ls)
    ls.append(root.val)
