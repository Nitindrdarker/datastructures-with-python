class node():
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedList():
    def __init__(self):
        self.head = None
        self.count = 0
    def addNode(self, data):
        self.count += 1
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
#recursiev function to add the linkedlist from last node ot manage carry
def addlist(list1, list2, list3, carry):
    if list1 != None and list2 != None:
        carry = addlist(list1.next, list2.next, list3, carry)
        currentsum = list1.data + list2.data + carry
        carry = currentsum // 10
        lastdigit = currentsum % 10
        temp = node(lastdigit)
        temp.next = list3.head
        list3.head = temp
    return carry
#function to add node of first carry at the end of execution
def headdercarry(list1, list2, list3, carry):
    carry = addlist(list1, list2, list3, 0)
    if carry > 0:
        car = node(carry)
        car.next = list3.head
        list3.head = car
#function to equalise the both linked lists so that we can call addlist function later
def controlSystem(list1, list2):
    difference = abs(list1.count - list2.count)
    if list1.count > list2.count:
        for i in range(difference):
            temp = node(0)
            temp.next = list2.head
            list2.head = temp
    elif(list1.count < list2.count):
        for i in range(difference):
            temp = node(0)
            temp.next = list1.head
            list1.head = temp


list1 = linkedList()
list1.addNode(9)
list1.addNode(9)
list1.addNode(9)
list1.addNode(9)
list2 = linkedList()
list2.addNode(1)
list2.addNode(1)
list2.addNode(1)
list2.addNode(1)
controlSystem(list1, list2)
list3 = linkedList()
headdercarry(list1.head, list2.head, list3, 0)
list3.display()
# 8 6 8
#+0 0 5
#-------
# 8 6 8
#
# 
# .
# 8 6 8
# 9 9 9 9
# 1 1 1 1
#+
#----------
#1 1 1 1 0    