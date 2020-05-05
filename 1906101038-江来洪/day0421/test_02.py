#前序遍历
ls = []
def pre(root,ls):
    #如果节点为空（叶子节点）
    if not root:
        return
    ls.append(root.val)
    pre(root.left,ls)
    pre(root.right,ls)

#中序遍历
ls1 = []
def mid(root,ls1):
    if not root:
        return
    mid(root.left,ls1)
    ls1.append(root.val)
    mid(root.right,ls1)

#后序遍历
ls2 = []
def pos(root,ls1):
    if not root:
        return
    pos(root.left,ls1)
    pos(root.right,ls1)
    ls2.append(root.val)
