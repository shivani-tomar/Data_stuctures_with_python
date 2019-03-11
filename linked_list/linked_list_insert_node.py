import config as con
import linked_list_create_node as cn
#import linked_list_traverse as trav


class insert:
    start = None
    def __init__(self):
        self.start = con.head
        print("self start in insert is ")
        print(self.start)

    def insertAtFirst(self,data):
        temp = cn.Node(data)
        temp.next = con.head
        con.head = temp
        print("data is inserted")
        print(con.head.data)
        
    def insertAtLast(self , data):
        temp =  cn.Node(data)
        starts = self.start
        while(starts.next != None):
            starts = starts.next
        starts.next = temp
        starts = starts.next    

    def insertAtPosition(self, pos, data):
        temp = cn.Node(data)
        starts = self.start
        count = 1
        while(count != pos-1):
            starts = starts.next
            count+=1
        temp.next = starts.next
        starts.next = temp
        