#Pre order, middle order and post order
ls=[]
#前序遍历
def pre(root,ls):
    #如果结点为空(如果为叶子结点)
    if not root:
        return
    ls.append(root.val)#根
    pre(root.left,ls)#左
    pre(root.right,ls)#右

def mid(root,ls):
    if not root:
        return
    mid(root.left,ls)#左
    ls.append(root.val)#根
    mid(root.right,ls)#右

def post(root,ls):
    if not root:
        return
    post(root.left,ls)#左
    post(root.right,ls)#右
    ls.append(root.val)#根
    
