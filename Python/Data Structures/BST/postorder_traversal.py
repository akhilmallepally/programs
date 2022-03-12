def postorder_traversal(self, res):
    res = []
    if root!=None:
        postorder_traversal(self.left, res)
        postorder_traversal(self.left, res)
        res.append(root.data)
    return res
        
