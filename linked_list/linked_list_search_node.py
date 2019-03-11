import config as con

class search:
    start = None
    def __init__(self):
        self.start = con.head
        print("self start in search is ")
        print(self.start)

    def searchLinkedlist(self , data):
        print("data is")
        print (data)
        starts = self.start
        if starts == None:
            print("Linked list is empty")
        else:
            count = 1
            flag = 0
            while(starts):
                if starts.data == data:
                    print("%s is found at %d" %(starts.data , count))
                    flag = 1
                    break
                else:
                    starts = starts.next
                    count+=1
            if  flag == 0:
                print("data is not in linked list")

