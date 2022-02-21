class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BuildBst:
    def build_bst(self, root, ele):
        if root == None:
            return Node(ele)
        elif root.data>ele:
            root.left = self.build_bst(root.left, ele)
        else:
            root.right = self.build_bst(root.right, ele)
        return root
    def inorder(self, root):
        if root == None:
            return
        else:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
root = None
b = BuildBst()
lst = [3,1,4,5,3,3,72,67]
for ele in lst:
    root = b.build_bst(root, ele)
b.inorder(root)
