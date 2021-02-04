class LinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    #enqueue method
    ## add to back of line
    def enqueue(self, item):
        new_node = LinkedListNode(item)
        #check if queue if empty
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            #add new node to rear
            self.rear.next = new_node
            #reassign rear to new node
            self.rear = new_node
    
    #dequeue
    #take away from front of line
    def dequeue(self):
        if self.front is not None:
            #keep copy of old front
            old_front = self.front
            self.front = old.front.next
            
        #check if the queue is now empty
        if self.front is None:
            #make sure rear is also None
            self.rear = None
            
        return  old_front
    