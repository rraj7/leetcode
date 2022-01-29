class queue: 
    def __init__(self, capacity):
        self.front = self.size = 0 
        self.rear = capacity - 1 
        self.q = [None]*capacity
        self.capacity = capacity


    # when size = capacity
    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0
    
    def enQueue(self, item):
        if self.isFull():
            print('Full')
            return 
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = item
        self.size = self.size + 1 
        print("% s enqeued to the queue" % str(item))
    
    def deQueue(self):
        if self.isEmpty():
            print("empty")
            return 
        print ("% s dequeud from the queue " % str(self.q[self.front]))
        self.front = (self.front + 1 ) % (self.capacity)
        self.size = self.size - 1