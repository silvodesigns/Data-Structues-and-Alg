"""

Understand:

mySet= MyHashSet()
mySet.add(1) {1}
mySet.add(2) {1, 2}
mySet.contains(1) True
mySet.remove(1) {2}
mySet.contains(1) False
mySet.contains(2) True
Plan:
    Init
            Initialize the list with a static size
    Add
            Run key through the hash function and store key in List
            using the index from the hash function
    Contains
            Run key through hash function to get the hash index
            Check list at hashIndex to see if something is stored there
    Remove 
            Run key through hash function. Make value at hashIndex to None
            
"""
from collections import deque

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [None] * 10000
        

    def add(self, key: int) -> None:
        hashIndex = hash(key) % len(self.table)
        if self.table[hashIndex] == None:
            newList = deque()
            newList.append(key)
            self.table[hashIndex] = newList 
        elif key not in self.table[hashIndex]:
            self.table[hashIndex].append(key)
            
    def remove(self, key: int) -> None:
        hashIndex = hash(key) % len(self.table)
        if self.table[hashIndex] != None:
            try:
                self.table[hashIndex].remove(key)
            except:
                pass
        


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashIndex = hash(key) % len(self.table)
        if self.table[hashIndex] != None:
            return key in self.table[hashIndex]
        return False
       
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)