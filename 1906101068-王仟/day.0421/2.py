#Pre ordre,middle order and post order
Is=[]
def pre(root,Is):
    if not root:
        return
    Is.append(root,val)
    pre(root.left,Is)
    pre(root.right,Is)

def mid(root,IS):
    if not root:
        return
    pre(root.left,Is)
    Is.append(root.val)
    pre(root.right,Is)

def post(root,Is):
    if not root:
        return
    post(root.left,IS)
    post(root.right,Is)
    Is.append(root,val)