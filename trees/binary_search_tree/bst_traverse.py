class Traverse:
    def __init__(self):
        print("I am in Traverse")
    def inorderTraverse(self, root):
        if not root:
            return
        else:
            self.inorderTraverse(root.left)
            print(root.data)
            self.inorderTraverse(root.right)

    def preorderTraverse(self, root):
        if not root:
            return
        else:
            print(root.data)
            self.preorderTraverse(root.left) 
            self.preorderTraverse(root.right)

    def postorderTraverse(self, root):
        if not root:
            return
        else:
            self.postorderTraverse(root.left) 
            self.postorderTraverse(root.right)
            print(root.data)