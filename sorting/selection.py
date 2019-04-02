class Selection:
    def __init__(self , lists):
        print("this is selection sort example")
        self.lists = lists
    def selection(self):
        size = len(self.lists);
        swapcount =0;
        for i in range(0,size):
            minimum = i;
            #print("i is" , i);
            for j in range(i+1 , size):
                #print("j is " ,j);
                if self.lists[minimum]<self.lists[j]:
                    minimum = j;
        self.lists[minimum] , self.lists[i] = self.lists[i],self.lists[minimum] 
        swapcount+=1;
        print(swapcount);
        print(self.lists);
    
    
