class Search:
    def __init__(self):
        print("I am in Search")

    def searchBst(self , root , data):
        if not root:
            return
        else:
            if root.data == data:
                print("data is found %d " %(root.data))
            elif data > root.data:
                self.searchBst(root.right , data)
            elif data < root.data:
                self.searchBst(root.left , data)