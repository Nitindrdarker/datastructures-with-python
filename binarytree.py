class Node: 
    def __init__(self, key): 
        self.left = None
        self.right = None
        self.val = key 
  

  
def insert(root, key): 
    if root is None: 
        return Node(key) 
    else: 
        if root.val == key: 
            return root 
        elif root.val < key: 
            root.right = insert(root.right, key) 
        else: 
            root.left = insert(root.left, key) 
    return root 
  
  
  
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

def find_min(root):
    if root.left is not None:
        return find_min(root.left)
    return root.val
def find_max(root):
    if root.right is not None:
        return find_max(root.right)
    return root.val
def height(root):
    if(root == None):
        return -1
    else:
        left_node = height(root.left)
        right_node = height(root.right)
        return max(left_node,right_node)+1
def breadth_first_travarsal(root):
    if root == None:
        print('empty bst')
        return 
    q = []
    
    q.append(root)
    
    
    while(q):
       
        current = q.pop(0)
        print(current.val)
        if(current.left != None):
            q.append(current.left)
        if(current.right != None):
            q.append(current.right)
            
        
    
                



  

r = Node(50) 
r = insert(r, 30) 
r = insert(r, 20) 
r = insert(r, 40) 
r = insert(r, 70) 
r = insert(r, 60) 
r = insert(r, 80) 
r = insert(r,0)
  
# Print inoder traversal of the BST 
print('inorder')
inorder(r) 
print('preorder')
preorder(r)
print('postorder')
postorder(r)
print('min = ',find_min(r))

print('max = ',find_max(r))
print('height = ',height(r))
print('breadth_first_travarsal')
breadth_first_travarsal(r)