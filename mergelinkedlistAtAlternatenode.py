class node():
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedList():
    def __init__(self):
        self.head = None
        
    def addNode(self, data):
        
        new_node = node(data)
        temp = self.head
        if temp == None:
            temp = new_node
            self.head = temp
            return
        while(temp.next != None):
            temp = temp.next
        temp.next = new_node
    def display(self):
        temp = self.head
        while(temp != None):
            print(temp.data, end=" ")
            temp = temp.next
    def merge(self, q): 
		
        q_current = q.head
        p_current = self.head
		# While there are available positions in p; 
        while p_current != None and q_current != None:

			# Save next pointers 
	        p_next = p_current.next
	        q_next = q_current.next

			# make q_curr as next of p_curr
	        q_current.next = p_next # change next pointer of q_curr
	        p_current.next = q_current # change next pointer of p_curr

			# update current pointers for next iteration 
	        p_current = p_next
	        q_current = q_next
        q.head = q_current

list1 = linkedList()
list2 = linkedList()

list1.addNode(1)
list2.addNode(2)
list1.addNode(1)
list2.addNode(2)
list1.addNode(1)
list2.addNode(2)

list1.merge(list2)
list1.display()
list2.display()