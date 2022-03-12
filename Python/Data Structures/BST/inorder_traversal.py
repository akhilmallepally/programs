def inorder_traversal(self, res):
    res = []
    
    if root!= None:
        inorder_traversal(self.left, res)
        res.append(root.data)
        inorder_traversal(self.right, res)
    return res
