def back(root,ls):
    if not root:
        return
    back(root.left,ls)
    
    back(root.right,ls)
    ls.append(root.val)