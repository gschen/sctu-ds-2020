#Pre order, middle order and post order
ls=[]
#前序遍历
def pre(root,ls):
#如果结点为空(如果为叶子结点)
    if not root:
        return
    ls.append( root.val)
    pre(root.left,ls)
    pre( root.right,ls)
def mid(root,ls):
    if not root:
        return
    mid(root.left,ls)
    ls.append(root.val)
    mid(root.right,ls)
def post(root,ls):
    if not root:
        return
    post(root.left,ls)
    post(root.right,ls)
    ls.append(root.val)