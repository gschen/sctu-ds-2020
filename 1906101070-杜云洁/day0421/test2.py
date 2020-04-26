#遍历:pre_order,middle order,post order
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
def middle(root,ls):
    if not root:
        return 
    pre(root.left,ls)
    ls.append(root.val)
    pre(root.right,ls)
#后序遍历       
def post(root,ls):
    if not root:
        return 
    pre(root.left,ls)
    pre(root.right,ls)
    ls.append(root.val)
               
    
    
    
        