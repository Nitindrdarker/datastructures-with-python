class node():
    def __init__(self, data):
        self.data = data
        self.next = None
def dispaly(head):
    while(head):
        print(head.data)
        head = head.next
def compare(list1, list2):
    while(list1 and list2 and list1.data == list2.data):
        list1 = list1.next
        list2 = list2.next
    if list1 and list2:
        return 1 if list1.data > list2.data else -1
    if list1 and not list2:
        return 1
    if list2 and not list1:
        return -1
    return 0
n = node('n')
n.next = node('i')
n.next.next = node('t')
n.next.next.next = node('i')
n.next.next.next.next = node('s')
n1 = node('n')
n1.next = node('i')
n1.next.next = node('t')
n1.next.next.next = node('i')
n1.next.next.next.next = node('s')
print(compare(n, n1))


    


        
        