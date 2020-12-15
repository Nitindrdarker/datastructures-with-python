class Node:
    def __init__(self,d):
        self.data = d
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
def insert_node(head):
    while(head.next != None):
        head = head.next
    d = int(input('enter the numebr you want to append at the end'))
    head.next = Node(d)
def delete(head):
    v = int(input('enter the numebr you want ot delete'))
    while(head.next.data != v):
        head = head.next
    temp = head.next
    head.next = temp.next
    del temp        
def delete_first(head):
    temp = head
    head = head.next
    del temp
    return head
def beginning_insert(head):
    d = int(input("enter the number you want to insert at the beginning"))
    beginning_node = Linkedlist() 
    beginning_node.head = Node(d)
    beginning_node.head.next = head
    return beginning_node.head
def dispaly(head):
    while(head != None):
        print(head.data)
        head = head.next
first = Linkedlist()
first.head = Node(1)
second = Node(2)
third = Node(3)
first.head.next = second
second.next = third
insert_node(first.head)
first.head = beginning_insert(first.head)
first.head = delete_first(first.head)
dispaly(first.head)
delete(first.head)
dispaly(first.head)


