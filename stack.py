class node():
    def __init__(self,d):
        self.data = d
        self.next = None
class Stack():
    
    def __init__(self):
        self.head = None
    def push_stack(self,d):
        new_node = node(d)
        if(self.head == None):
            self.head = new_node
        else:
            last = self.head
            while(last.next != None):
                last = last.next
            last.next = new_node
    def display_stack(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next
    def pop_stack(self): 
        
        if(self.head.next == None):
            self.head = None
        temp = self.head    
        while(temp.next.next !=None):
            temp = temp.next
            
        temp.next = None
    def peek_stack(self):
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        print(temp.data)









stk = Stack()
stk.push_stack(1)
stk.push_stack(2)
stk.push_stack(3)
stk.push_stack(4)
stk.display_stack()
stk.pop_stack()

stk.display_stack()
stk.push_stack(6)
stk.display_stack()
stk.pop_stack()
stk.display_stack()
stk.push_stack(10)
stk.peek_stack()

            







        


