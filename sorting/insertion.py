class Insertion:
    def __init__(self ,lists):
        print("this is insertion sort example")
        self.lists = lists
    def insertion(self):
        size = len(self.lists);
        for i in range(size):
            temp = self.lists[i];
            j = i;
            while(j>0  and temp<self.lists[j-1]):
                self.lists[j] = self.lists[j-1];
                j-=1;
            self.lists[j] = temp;
        print(self.lists);


