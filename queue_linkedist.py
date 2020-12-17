class node():
    def __init__(self,d):
        self.data = d
        self.link = None

class queue():
    def __init__(self):
        self.head = None
    def enqueu(self,d):
        new_node = node(d)
        if(self.head == None):
            self.head = new_node
        
        else:
            
            last = self.head
            while(last.link != None):
                
                last = last.link
            last.link = new_node
    def dequeue(self):
        
        if(self.head == None):
            print('empty queue')
        else:
            temp = self.head
            self.head = self.head.link
            temp = None
            
       

        

    def display(self):
        n = self.head
        while(n != None):
            print(n.data)
            n = n.link




q = queue()
q.enqueu(1)
q.enqueu(2)
q.dequeue()
q.enqueu(3)
q.enqueu(4)

q.display()

q.dequeue()
print('------------')
q.display()
