#pre orderr,middle order and post order
Is=[]
def pre(root,Is):
    #
    if not root:
        return
    Is.append(root.val)
    pre(root.left,Is)
    pre(root.right,Is)
def mid(root,Is):
    if not root:
        return
    mid(root.left,Is)
    Is.append(root.val)
    mid(root.right,Is)