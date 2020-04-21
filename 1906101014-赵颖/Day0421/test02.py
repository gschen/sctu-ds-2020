#Pre order,middle order and post order
#遍历
#前
ls=[]
def pre(root):
    if not root:
        return
    ls.append(root.val)
    pre(root.left,ls)
    pre(root.right,ls)
#中
def mid(root,ls):
    if not root:
        return
    mid(root.left,ls)
    ls.append(root.val)
    mid(root.right,ls)
#后
def las(root,ls):
    if not root:
        return
    las(root.left,ls)
    las(root.right,ls)
    ls.append(root.val)
  