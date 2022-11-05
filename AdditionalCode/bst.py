# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:13:57 2021

@author: Swamy
"""

from treenode import TreeNode

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def num_nodes(self):        
        return self.size
    
    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        
        self.size = self.size + 1
    
    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left_child:
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)
        else:
            if current_node.right_child:
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)
                
    def get(self, key):
        
        if self.root:
            result = self._get(key, self.root)
            
            if result:
                return result.value
            
            return None

    def _get(self, key, current_node):
        
        if not current_node:
            return None
        
        if current_node.key == key:
            return current_node
        
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)


bst = BinarySearchTree()
bst.put(4, 2)
bst.put(13, 3)
bst.put(41, 12)
bst.put(3, 6)
bst.put(24, -5)
bst.put(-3, 23)

print(bst.num_nodes())
print(bst.get(4))

print(bst.get(41))

        