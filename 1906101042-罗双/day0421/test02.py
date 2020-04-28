#遍历
#Pre order,middle order and post order
ls=[]
#前序遍历
def pre(root,ls):
    #如果节点为空（如果为叶子节点）
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
def post(root,ls):
    if not root:
        return
    post(root.left,ls)
    post(root.right,ls)
    ls.append(root.val)