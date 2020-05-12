def pre(root,res):
    if not root:
        return
    res.append(root.val)
    pre(root.right,res)
    pre(root.left,res)
def getAIIElements(root1,root2):
    res = []
    pre(root1,res)
    pre(root2,res)
    return sorted(res)