ls=[]
def pre(root,ls):
    if not root:
        return 
    ls.append(root.val)
    pre(root.left,ls)
    pre(root.right,ls)

def mid(root,ls):
    if not root:
        return
    mid(root.left,ls)
    ls.append(root.val)
    mid(root.right,ls)
    
def end(root,ls):
    if not root:
        return
    end(root.left,ls)
    end(root.right,ls)
    ls.append(root.val)