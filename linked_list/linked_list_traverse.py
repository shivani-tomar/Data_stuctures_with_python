#import linked_list_create_node as cn
import config as con
class traverse:
    start = None
    def __init__(self):
        self.start = con.head
        print("self start in traverse is ")
        print(self.start)

    def trackLinkedlist(self):
        starts = con.head
        print("I am in traverse")
        #print(starts.data)
        while(starts):
            print(starts.data)
            starts = starts.next