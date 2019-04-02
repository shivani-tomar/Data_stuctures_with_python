class Bubble:
    def __init__(self, lists):
        print("this is bubble sort example")
        self.lists = lists
    def bubble(self):
        size = len(self.lists)
        print(self.lists , size)
        swapcount =0;
        for i in range(size):
            for j in range(size-i-1):
                if self.lists[j]>self.lists[j+1]:
                    self.lists[j] = self.lists[j]^self.lists[j+1];
                    self.lists[j+1] = self.lists[j]^self.lists[j+1];
                    self.lists[j] = self.lists[j] ^ self.lists[j+1];
                    swapcount+=1;
        print (swapcount)
        print(self.lists)
    
    
