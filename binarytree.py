class node():
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None
def display(root):
    if root:
        display(root.left)
        print(root.data)
        display(root.right)
def invert_bt(root):
    if root:
        invert_bt(root.left)
        invert_bt(root.right)

        root.left, root.right = root.right, root.left





r = node(0)
r.left = node(1)
r.right = node(2)
r.left.left = node(3)
r.right.right = node(4)
display(r)
invert_bt(r)
print('----------------')
display(r)