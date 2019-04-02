import bst_create_node as bcn
import bst_search as bs
import bst_traverse as bt
import bst_delete as bd

root = bcn.Node(75)
bst = bcn.insertNode()
bst.insertNode(root , 78)
bst.insertNode(root , 19)
bst.insertNode(root , 25)
bst.insertNode(root , 68)
bst.insertNode(root , 1)

bst.insertNode(root , 2)
bst.insertNode(root , 5)
bst.insertNode(root , 20)
bst.insertNode(root , 11)
bst.insertNode(root , 64)
bst.insertNode(root , 19)

trav = bt.Traverse() 
print("Inorder Traversal")
trav.inorderTraverse(root)

print("preorder Traversal")
trav.preorderTraverse(root)

print("postorder Traversal")
trav.postorderTraverse(root)

search = bs.Search()
print("searching in BST")
search.searchBst(root , 25)

delete = bd.Delete()
print("delete in BST")
#print(delete.findMin(root))
delete.deleteNode(root , 25)
trav.inorderTraverse(root)