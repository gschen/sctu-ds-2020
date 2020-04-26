#前序遍历
Is=[]
def pre(root,Is):
    #如果节点为空(如果为叶子节点)
    if not root:
        return
    Is.append(root.val)
    pre(root.left,Is)
    pre(root.right,Is)
#中序遍历
def mid(root,Is):
    if not root:
        return
    mid(root.left,Is)
    Is.append(root,val)
    mid(root.right,Is)
#后序遍历
def behind(root,Is):
    if not root:
        return
    behind(root.left,Is)
    behind(root.right,Is)
    Is.append(root,val)
   




