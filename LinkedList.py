from merge_sorted_ll import *

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
    
    #Append method
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def merge2(self, ll):
        merge_sorted(self,ll)
        
llist = LinkedList()
llist2 = LinkedList()

llist.append(1)
llist.append(3)
llist.append(5)
llist.append(8)

llist2.append(2)
llist2.append(4)
llist2.append(7)




#llist.print_list()  
#llist2.print_list() 

llist.merge2(llist2) 
llist.print_list()

