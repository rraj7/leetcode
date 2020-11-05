#Double Linkedlist

class Node: 
    def __init__(self);
    self.val = val 
    self.next = None
    self.prev = None 

#adding to the front: 
def push(new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    new_node.prev = None


    if self.head is not None: 
        self.head.prev = new_node
    
    self.head = new_node

def insertAfter(prev_node,new_node):
    if prev_node is None: 
        print(" Not exisit ")
        return 
    
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node
    new_node.prev = prev_node

    if new_node.next is not None: 
        new_node.next.perv = new_node