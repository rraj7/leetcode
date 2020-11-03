class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key 
    

def Inorder(root): #L-->Root--> Right
        if root:
            Inorder(root.left)
            print(root.val)
            Inorder(root.right)
    
def Postorder(root):    #Left --> Right --> Root
    if root: 
        Postorder(root.left)
        Postorder(root.right)
        print(root.val)

def Preorder(root):     #Root-->Left-->Right
    if root: 
        print(root.val)
        Preorder(root.left)
        Preorder(root.right)





#print(Preorder(root))
#print(Inorder(root))
#print(Postorder(root))

## How to find out the diameter of the tree: 

def height(root):
    if root is None :
        return 0
    return  1+ max(height(root.left), height(root.right))


def diameter(root):
    if root is None: 
        return 0
    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    return max(lheight+rheight+1, max(ldiameter,rdiameter))





root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right= Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(height(root))
# Given Tree: 
""" 
         1
      /    \
    2        3
  /   \    /   \
4      5  6     7 

"""