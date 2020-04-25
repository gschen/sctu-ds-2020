Is=[]
def pre(root,Is):#前序
    if not root:
        return
    Is.append(root.val)
    pre(root.left,Is)
    pre(root.right,Is)

def mid(root,Is):
    if not root:
        return
    pre(root.left,Is)
    Is.append(root.val)
    mid(root.right,Is)

def post(root,Is):
    if not root:
        return
    pre(root.left,Is)
    post(root.right,Is)
    Is.append(root.val)