
class ternary_search:
    def __init__(self, list , target):
        self.list = list
        self.target = target
    def ternary_search(self):
        low = 0
        high = len(self.list)
        while(low < high):
            mid1 = int((low+high)/3)
            print(mid1)
            mid2 = int((mid1+high)/3)
            print(mid2)
            if self.target == mid1:
                print("%s is found at %d" %(self.target , mid1+1))
                break
            elif self.target == mid2:
                print("%s is found at %d" %(self.target , mid2+1))
                break
            elif self.target < mid1:
                high = mid1
            elif self.target > mid2:
                low = mid2 + 1
            elif self.target > mid1 and self.target < mid2:
                low = mid1 + 1
                high = mid2
            # elif self.target == mid1:
            #     print("%s is found at %d" %(self.target , mid1+1))
            #     break
            # elif self.target == mid2:
            #     print("%s is found at %d" %(self.target , mid2+1))
            #     break
  
        else:
            print("Item is not in list")

