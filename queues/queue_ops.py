class queue:
    front = rear = -1
    max = 10
    def __init__(self):
        queue = list()

    def insert(self,data):
        if self.rear >= self.max:
            print("queue is full")
        else:
            self.rear = self.rear + 1
            self.queue[self.rear] = data

    def delete(self , data):
        if self.front == self.rear:
            print("queue is empty")
        else:
            temp = self.queue[self.front]
            self.front = self.front + 1


    def display(self):
        pointer = self.front:
        if self.front != self.rear:
            while(pointer != rear):
                print(self.queue[pointer])
                pointer = pointer + 1
        else:
            print("nothing to traverse")
