class node():
    def __init__(self, value):
        self.data = value
        self.next = None
class linkedList():
    def __init__(self):
        self.head = None
    def deleteNode(self, data):
        temp = self.head
        prev = self.head
        if temp.data == data:
            if temp.next == None:
                print("Only one node exists! cant delete")
            else:
                self.head = self.head.next
            return
        while(temp.next is not None and temp.data != data):
            prev = temp
            temp = temp.next
        if(temp.next is None and temp.data != data):
            print("node dosnt exist")
        elif(temp.next is None and temp.data == data):
            prev.next = None
        else:
            prev.next = temp.next
    def push(self, new_data): 
        new_node = node(new_data)
        temp = self.head
        if temp == None:
            temp = new_node
            self.head = temp
            return
        while(temp.next != None):
            temp = temp.next
        temp.next = new_node
        
        
    def PrintList(self): 
  
        temp = self.head 
        while(temp): 
            print(temp.data, end = " ") 
            temp = temp.next
llist = linkedList() 
llist.push(3) 
llist.push(2) 
llist.push(6) 
llist.push(5) 
llist.push(11) 
llist.push(10) 
llist.push(15) 
llist.push(12)
llist.PrintList()
print("deleteing 3")
llist.deleteNode(3)
llist.PrintList()
print("deleteing 11")
llist.deleteNode(11) 
llist.PrintList()
print("deleteing 12")
llist.deleteNode(12) 
llist.PrintList()


                