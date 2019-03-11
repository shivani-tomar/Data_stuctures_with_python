import config as con

head =  con.head
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        print("node is initialized with data %s" %(self.data))


class linkedList:
    #global head =  None
    start = None
    def __init__(self):
        self.head = None
        print("head is initialized with None")
        

    def insertNode(self , data):
        if self.head == None:
            self.head = Node(data)
            con.head = self.head
            print("I AM CON HEAD")
            print(con.head.data)
            self.start = self.head
            print("first node is created")
            print(self.start)
        else:
            print("I am in else")
            #print(self.start)
            temp = Node(data)
            self.start.next = temp
            self.start = temp

    
    # def trackLinkedlist(self):
    #     starts = self.head
    #     while(starts):
    #         print(starts.data)
    #         starts = starts.next



# def main():

#     linked_list = linkedList()
#     linked_list.insertNode("1")
#     linked_list.insertNode("2")
#     linked_list.insertNode("3")
#     linked_list.insertNode("4")
#     linked_list.insertNode("5")
#     linked_list.insertNode("6")
#     linked_list.insertNode("7")
#     linked_list.trackLinkedlist()



# if __name__ == "__main__":
#     main()


print("linked list creation and traversing")
print(__name__)







