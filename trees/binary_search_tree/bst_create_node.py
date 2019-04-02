class Node:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None
        print("Node is created with data %d" %(self.data))

class insertNode:
    def __init__(self):
        print("root is initialized")

    def insertNode(self ,node , data):
        if data < node.data and node.left == None:
            node.left = Node(data)
        elif data > node.data and node.right == None:
            node.right = Node(data)
        elif data < node.data and node.left != None:
            self.insertNode(node.left , data)
        elif data > node.data and node.right != None:
            self.insertNode(node.right , data)

    # def inorderTraverse(self, root):
    #     if not root:
    #         return
    #     else:
    #         self.inorderTraverse(root.left)
    #         print(root.data)
    #         self.inorderTraverse(root.right)

    # def preorderTraverse(self, root):
    #     if not root:
    #         return
    #     else:
    #         print(root.data)
    #         self.preorderTraverse(root.left) 
    #         self.preorderTraverse(root.right)

    # def postorderTraverse(self, root):
    #     if not root:
    #         return
    #     else:
    #         self.postorderTraverse(root.left) 
    #         self.postorderTraverse(root.right)
    #         print(root.data)

    # def searchBst(self , root , data):
    #     if not root:
    #         return
    #     else:
    #         if root.data == data:
    #             print("data is found %d " %(root.data))
    #         elif data > root.data:
    #             self.searchBst(root.right , data)
    #         elif data < root.data:
    #             self.searchBst(root.left , data)
            

    # def deleteNode(self , root , data):
    #     if not root:
    #         return
    #     elif data > root.data:
    #         self.deleteNode(root.right , data)
    #     elif data < root.data:
    #         self.deleteNode(root.left , data)
    #     elif  root.right == None:

       

# root = Node(75)
# bst = insertNode()
# bst.insertNode(root , 78)
# bst.insertNode(root , 19)
# bst.insertNode(root , 25)
# bst.insertNode(root , 68)
# bst.insertNode(root , 1)

# bst.insertNode(root , 2)
# bst.insertNode(root , 5)
# bst.insertNode(root , 20)
# bst.insertNode(root , 11)
# bst.insertNode(root , 64)
# bst.insertNode(root , 19)

# print("Inorder Traversal")
# bst.inorderTraverse(root)

# print("preorder Traversal")
# bst.preorderTraverse(root)

# print("postorder Traversal")
# bst.postorderTraverse(root)

# print("searching in BST")
# bst.searchBst(root , 10)


        
