# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:20:07 2021

@author: Swamy
"""
#homework 4 tree class
#treenode modified for homework 3 solutions
#with getters/setters

class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.balanceFactor = 0
        self.value = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def get_right_child(self):
        return self.rightChild
    
    def get_left_child(self):
        return self.leftChild
     
    def set_right_child(self, r):
        self.rightChild = r
   
    def set_left_child(self, l):
        self.leftChild = l
   
    def set_parent(self, p):
        self.parent = p
    
    def get_parent(self):
        return self.parent
     
    def get_key(self):
        return self.key
     
    def isLeftChild(self):
        return self.parent and self.parent.leftChild is self

    def isRightChild(self):
        return self.parent and self.parent.rightChild is self

    def isRoot(self):
        return not self.parent

    def is_leaf(self):
        return not (self.rightChild or self.leftChild)
    
    def hasRightChild(self):
        return self.rightChild
    
    def hasLeftChild(self):
        return self.leftChild
    
    def has_a_child(self):
        return self.rightChild or self.leftChild

    def has_children(self):
        return self.rightChild and self.leftChild

    def replace_value(self, key, value, left, right):
        self.key = key
        self.value = value
        self.leftChild = left
        self.rightChild = right
        if self.leftChild:
            self.leftChild.parent = self
        if self.rightChild:
            self.rightChild.parent = self