ls = []
# 前序遍历
def pre(root, ls):
    # 如果结点为空(如果为叶子结点)
    if not root:
        return
    # 根
    ls.append(root.val)
    # 左
    pre(root.left, ls)
    # 右
    pre(root.right, ls)

def mid(root, ls):
    if not root:
        return
    # 左
    mid(root.left, ls)
    # 根
    ls.append(root.val)
    # 右
    mid(root.right, ls)

def post(root, ls):
    if not root:
        return
    # 左
    post(root.left, ls)
    # 右
    post(root.right, ls)
    # 根
    ls.append(root.val)