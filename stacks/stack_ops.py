class stacks:
    top = -1
    max = 10
    def __init__(self):
        self.lists = list()

    def insert(self , data):
        if self.top >= self.max:
            print("stack is overflow")
        else:
            self.top = self.top + 1
            #print(self.top , self.lists)
            self.lists[self.top] = data
            #print(self.lists[top])
            print("%s data is inserted at %d" %(data , self.top + 1))

    def display(self):
        tops = self.top
        while(tops != -1):
            print(self.lists[tops])
            tops = tops - 1
          

    def delete (self):
        if self.top == -1:
            print("stack is empty")
        else:
            data = self.lists[self.top]
            self.top= self.top - 1
            print("data is %s")
            print(data)


        

