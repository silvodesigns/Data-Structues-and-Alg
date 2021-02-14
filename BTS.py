#Binary Search Tree
from Queue2 import Queue
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
                
    def search(self, target):
        
        if self.value == target:
            return self
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.searhc(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(target)
    
class BST:
    def __init__(self, value):
        self.root = BSTNode(value)
    
    def insert(self, value):
        self.root.insert(value)
        
    def search(self, value):
        self.root.search(value)
        
    def pre_order(self, node, traverse):
        """root, left , right"""
        if node:
            traverse += (str(node.value) + "--")
            traverse = self.pre_order(node.left, traverse)
            traverse = self.pre_order(node.right, traverse)
        return traverse
    
    
    def in_order(self, node, traverse):
        """left, root , right"""
        if node:
            traverse = self.in_order(node.left, traverse)
            traverse += (str(node.value) + "--")
            traverse = self.in_order(node.right, traverse)
        return traverse
    
    def post_order(self, node, traverse):
        "left, right, root"
        if node:
            traverse = self.post_order(node.left, traverse)
            traverse = self.post_order(node.right, traverse)
            traverse += (str(node.value) + "--")
        return traverse
      
    def level_order(self, node):
        if node is None:
            return
        
        queue = Queue()
        queue.enqueue(node)
        
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "--"
            node = queue.dequeue()
            
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

#Binary Tree Traversal
tree = BST(1)
tree.root.right = BSTNode(2)
tree.root.left = BSTNode(3)
tree.root.right.right = BSTNode(6)
tree.root.right.left = BSTNode(8)
tree.root.left.left = BSTNode(5)

print(tree.pre_order(tree.root, ""))
print(tree.in_order(tree.root, ""))
print(tree.post_order(tree.root, ""))
print(tree.level_order(tree.root))
