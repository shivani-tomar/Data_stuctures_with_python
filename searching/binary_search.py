class binary_search:
    def __init__(self, list , target):
        self.list = list
        self.target = target
    def binary_search(self):
        low = 0
        high = len(self.list)
        while(low < high):
            mid = int((low+high)/2)
            if self.list[mid] == self.target:
                print("%s is found at %d" %(self.target , mid+1))
                break
            elif self.list[mid] < self.target:
                low = mid+1
            else:
                high = mid
        else:
            print("Item is not in list")

