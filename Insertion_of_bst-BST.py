def insertIntoBST(root, val):
    if root == None:
        return TreeNode(val)
    elif root.data > val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    return root
