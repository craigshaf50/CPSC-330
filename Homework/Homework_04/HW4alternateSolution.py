# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 13:34:21 2021

@author: craig
"""
import random
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
# =============================================================================
# Counting the height
# =============================================================================
        self.height = 1

class AVLTree:
    def __init__(self):
        self.size = 0
# =============================================================================
# Count the number of left and right rotations
# =============================================================================
        self.numLeft = 1
        self.numRight = 1
        

    def num_nodes(self):
        return self.size
    
    def put(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.value:
             root.left_child = self.put(root.left_child, key)
        else:
            root.right_child = self.put(root.right_child, key)
        
        self.size = self.size + 1
        root.height = 1+ max(self.getHeight(root.left_child), 
                             self.getHeight(root.right_child))

# =============================================================================
# Update the balanceFactor        
# =============================================================================
        balanceFactor = self.updateBalance(root)
        
        if balanceFactor > 1 and key < root.left_child.value:
            return self.rotateRight(root)
        
        elif balanceFactor < -1 and key > root.right_child.value:
            return self.rotateLeft(root)
        
        elif balanceFactor > 1 and key > root.left_child.value:
            root.left_child = self.rotateLeft(root.left_child)
            return self.rotateRight(root)
        
        elif balanceFactor < -1 and key < root.right_child.value:
            root.right_child = self.rotateRight(root.right_child)
            return self.rotateLeft(root)
        
        return root
# =============================================================================
# Left Rotation   
# =============================================================================
    def rotateLeft(self,rotRoot):
        
        self.numLeft +=1

        newRoot = rotRoot.right_child
        temp = newRoot.left_child
        
        newRoot.left_child = rotRoot
        rotRoot.right_child = temp
        rotRoot.height = 1 + max(self.getHeight(rotRoot.left_child),
                                 self.getHeight(rotRoot.right_child))
        newRoot.height = 1 + max(self.getHeight(newRoot.left_child),
                                 self.getHeight(newRoot.right_child))
         
        return newRoot

# =============================================================================
# Right Rotation        
# =============================================================================
    def rotateRight(self,rotRoot):
        self.numRight = self.numRight + 1
        
        newRoot = rotRoot.left_child
        t2 = newRoot.right_child        
        
        newRoot.right_child = rotRoot
        rotRoot.left_child = t2

        rotRoot.height = 1 + max(self.getHeight(rotRoot.left_child),
                                 self.getHeight(rotRoot.right_child))
        newRoot.height = 1 + max(self.getHeight(newRoot.left_child),
                                 self.getHeight(newRoot.right_child))
        
        return newRoot
 
# =============================================================================
# Get the Height and Balance       
# =============================================================================
        
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
        
    def updateBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left_child) - self.getHeight(root.right_child)
# =============================================================================
# Take the total of left rotations and the total number of right 
# rotations and add them together        
# =============================================================================
    def numRotate(self,root):
        if not root:
            return 0
        return self.numLeft + self.numRight



avl2 = AVLTree()

avlList = random.sample(range(1,10001), 1001)#Generate a radom unique array of 1000 numbers
# =============================================================================
# Add the numbers to the list
# =============================================================================
root2 = None

for i in range(1001):
    root2 = avl2.put(root2, avlList[i])


# =============================================================================
# print(avlList) WILL SHOW ALL NUMBERS IN THE LIST
# =============================================================================

print("Rotations:",avl2.numRotate(root2))
print("Height of Tree:", avl2.getHeight(root2))
