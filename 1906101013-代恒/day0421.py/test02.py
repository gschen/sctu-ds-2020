#Pre order, middle order an post order
Is=[]
#前序遍历
def pre(root,Is):
    #如果节点为空(如果为叶子节点)
    if not root:
        return

        
    Is.append(root,val)
    pre(root,left,Is)
    pre(root,right,Is)
    
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
