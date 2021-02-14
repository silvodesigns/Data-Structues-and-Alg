
# Maximum Depth

from collections import deque
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    def __init__(self, value):
        self.root = BSTNode(value)
        
    def maxDepth(self, root):
        self.depth = 0
        self.helper(root, 1)
        return self.depth
    
    def helper(self, root, currDepth):
        if root == None:
            return 
        if root.left == None and root.right == None:
            if currDepth > self.depth:
                self.depth = currDepth
            return
        
        
        self.helper(root.left, currDepth + 1)
        self.helper(root.right, currDepth + 1)
    
    def maxDepth2(self, root: TreeNode) -> int:
        #iterative version
        if root == None:
            return 0
        stack = deque()
        stack.append((root, 1))
        maxDepthFound = 1
        while len(stack) > 0:
            curr = stack.pop() 
            currNode, currDepth = curr[0], curr[1]
            if currNode.left == None and currNode.right == None:
                if currDepth > maxDepthFound:
                    maxDepthFound = currDepth
            if currNode.left != None:
                stack.append((currNode.left, currDepth + 1))
            if currNode.right != None:
                stack.append((currNode.right, currDepth + 1))
        return maxDepthFound
    
    

tree = BST(1)
tree.root.right = BSTNode(2)
tree.root.left = BSTNode(3)
tree.root.right.right = BSTNode(6)
tree.root.right.left = BSTNode(8)
tree.root.left.left = BSTNode(5)
tree.maxDepth(tree.root)



