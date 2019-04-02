class Delete:
    def __init__(self):
        print("I am in delete")

    def findMin(self , root):
        min = root
        if not root:
            return
        else:
            while(root.left != None):
                    root = root.left
            return root


    def deleteNode(self , root , data):
        if not root:
            return
        elif data > root.data:
            self.deleteNode(root.right , data)
        elif data < root.data:
            self.deleteNode(root.left , data)
        else:
            if root.right == None and root.left == None:
                # root.data = None
                del root
            elif root.right == None:
                temp = root
                root = root.left
                del temp
            elif root.left == None:
                temp = root
                root = root.right
                del temp
            else:
                temp = self.findMin(root.right)
                temp2 = root
                root = temp
                del temp2
                del temp