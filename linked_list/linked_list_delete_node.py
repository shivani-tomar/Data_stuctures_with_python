import config as con

class delete:
    start = None
    def __init__(self):
        self.start = con.head
        print("self start in delete is ")
        print(self.start)

    def firstNodeDeletion(self):
        temp = con.head
        con.head = con.head.next
        del temp

    def lastNodeDeletion(self):
        starts = self.start
        while(starts.next.next != None):
            starts = starts.next
        temp = starts.next
        # print("TEMP LAST NODE DATA IS")
        # print(temp.data)
        starts.next = None
        del temp

    def deletionByPosition(self,pos):
        starts = con.head
        count = 1
        print(pos)
        while count != pos-1 and starts.next!= None and not pos <= 0 :
            # print("I am in loop")
            # print(starts.data , count)
            starts = starts.next
            count+=1

        temp = starts.next
        starts.next = starts.next.next
        print("TEMP LAST NODE DATA IS")
        print(temp.data)
        temp.next = None
        del temp

    

    def deletionByData(self,data):
        starts = self.start
        while starts.next != None:
            if starts.next.data == data:
                starts.next = starts.next.next
                temp = starts.next
                temp.next = None
                del temp
                break
            else:
                starts = starts.next
        
        else:
            print("data not found")