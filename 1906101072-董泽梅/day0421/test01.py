#Pre order,middle order and post order
ls = []
#前序遍历
def pre(root,ls):
    #如果节点为空（如果为叶子节点）s
    if not root:
        return
    ls.append(root.val)
    pre(root.left,ls)
    pre(root.right,ls)

#中序遍历
def mid(root,ls):
    if not root:
        return
    mid(root.left,ls)
    ls.append(root.val)
    mid(root.right,ls)

#后序遍历
def pos(root,ls):
    if not root:
        return
    pos(root.left,ls)
    pos(root.right,ls)
    ls.append(root.val)