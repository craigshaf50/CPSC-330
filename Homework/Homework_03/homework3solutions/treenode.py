# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:20:07 2021

@author: Swamy
"""
#treenode modified for homework 3 solutions
#with getters/setters

class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def get_right_child(self):
        return self.right_child
    
    def get_left_child(self):
        return self.left_child
     
    def set_right_child(self, r):
        self.right_child = r
   
    def set_left_child(self, l):
        self.left_child = l
   
    def set_parent(self, p):
        self.parent = p
    
    def get_parent(self):
        return self.parent
     
    def get_key(self):
        return self.key
     
    def is_left_child(self):
        return self.parent and self.parent.left_child is self

    def is_right_child(self):
        return self.parent and self.parent.right_child is self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_a_child(self):
        return self.right_child or self.left_child

    def has_children(self):
        return self.right_child and self.left_child

    def replace_value(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        if self.left_child:
            self.left_child.parent = self
        if self.right_child:
            self.right_child.parent = self