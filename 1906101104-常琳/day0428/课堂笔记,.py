ls=[]
#前序遍历
def pre(root,ls):
    #如果节点为空（如果为叶子节点）
    if not root:
        return
    ls.append(root.val)#根    
    pre(root.left,ls)#左
    pre(root.right,ls)#右 
    return ls
