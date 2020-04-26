ls=[]
def pre(root,ls):
    if not root:#如果节点为空，如果为叶子节点
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

def behi(root,ls):
    if not root:
        return 
    behi(root.left,ls)
    behi(root.right,ls)
    ls.append(root.val)
    