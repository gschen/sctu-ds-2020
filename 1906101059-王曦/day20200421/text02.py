# 前序 , 中序 ， 后序
ls = []
def pre(root, ls):
    if not root:
        return
    ls.append(root.val)
    pre(root.left, ls)
    pre(root.right, ls)

def mid(root, ls):
    if not root:
        return
    mid(root.left, ls)
    ls.append(root.val)
    pre(root.right, ls)

def post(root, ls):
    if not root:
        return
    mid(root.left, ls)
    pre(root.right, ls)
    ls.append(root.val)