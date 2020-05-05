#前序、中序和后续（Pre order、middle order、post order)
ls=[]
def pre(root,ls):#前序遍历
    if not root:#如果节点为空（叶子节点）
        return
    ls.append(root.val)
    pre(root.left,ls)
    pre(root.right,ls)
def mid(root,ls):#中序遍历
    if not root:
        return
    mid(root.left,ls)
    ls.append(root.val)
    mid(root.right,ls)    
def post(root,ls):#后序遍历
    if not root:
        return
    post(root.left,ls)
    ls.append(root.val)
    post(root.right,ls)