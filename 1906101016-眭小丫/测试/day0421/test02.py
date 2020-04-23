#遍历前序Pre order，中序Middle order，后序post order
ls=[]
#前序遍历
def pre(root,ls):
    if not root:#如果节点为空（如果为叶子节点）
        return
    #前序顺序根左右
    ls.append(root.val)
    pre(root.left,ls)
    pre(root.right,ls)


def mid(root,ls):
    if not root:
        return
    #中序顺序左根右
    mid(root.left,ls)
    ls.append(root.val)
    mid(root.right,ls)


def post(root,ls):
    if not root:
        return
    #后序顺序左右根
    post(root.left,ls)
    post(root.right,ls)
    ls.append(root.val)

