class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    #Printing nodes
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
    
    #Append node
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    #Delete node by value
    def delete(self, data):
        #If data is the head
        current_node = self.head
        
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        
        prev = None
        #update the values till they match
        while current_node and current_node.data != data:
            prev = current_node
            current_node = current_node.next
           
        #we we get out of the while loop and current_node.next is None , we did not 
        #found value to be deleted in the LinkedList 
        if current_node is None:
            return
        
        #If we did, we get to this point of the code
        prev.next = current_node.next
        current_node = None
         
    #Delete node by index/position
    def delete_pos(self, pos):
        #If the list has a head(is not empty)
        if self.head:  
            #Lets check if POS is the head
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return
        prev = None
        count = 0
        #Lets walk the LinkedList, untill we found the POS
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None
        
            
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")


llist.print_list()  
print(llist.self())