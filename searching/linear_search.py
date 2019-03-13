class linear_search:
    def __init__(self, list , target):
        self.list = list
        self.target = target
    def linear_search(self):
        for i in self.list:
            if i == self.target:
                print("Item is found.")
                break
        else:
            print("Item is not present in list.")