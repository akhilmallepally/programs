def preorder_traversal(self, res):
    res = []
    if root!=None:
        res.append(root.data)
        self.preorder_traversal(self.left, res)
        self.preorder_traversal(self.right, res)
    return res
