class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    class Stack:
        def __init__(self):
            self.top = None
            
        def push(self, data):
            #create a new node with data
            new_node = LinkedListNode(data)
            #set current top to new node's next
            new_node.next = self.top
            #reset the top pointet to the new node
            self.top = new_node
            
        def pop(self):
            if self.top is not None:
                #store popped node
                popped_node = self.top
                #reset top pointer to next node
                self.top = popped_node.next
                #return the value from the popped node
                return popped_node.data