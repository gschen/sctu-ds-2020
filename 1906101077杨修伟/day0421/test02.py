#遍历
#前序，中序，后序——pre order,middle oreder ,post order
ls=[]
#前序遍历
def pre(root,ls):
    #如果节点为空（如果为叶子节点）
    if not root:
        return 
    #前序
    ls.append(root.val)#根
    pre(root.left,ls)#左
    pre(root.right,ls)#右
#中序遍历
def mid(root,ls):
     #如果节点为空（如果为叶子节点）
    if not root:
        return 
    #中序
    mid(root.left,ls)#左
    ls.append(root.val)#根
    mid(root.right,ls)#右
#后序
def post(root,ls):
     #如果节点为空（如果为叶子节点）
    if not root:
        return
    #后序
    post(root.left,ls)#左
    post(root.right,ls)#右
    ls.append(root.val)#根