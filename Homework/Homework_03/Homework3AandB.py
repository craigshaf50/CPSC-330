# -*- coding: utf-8 -*-
#############################################################
# Homework 3 Problem A and B
# author: Craig Shaffer
# date revision: 9/30/21
# course: CPSC 330
#
# a. function will take a binary tree as input and return 
# the total number of nodes in the tree. The code must count
# the nodes by traversing the tree.
#
# b. function will take a binary tree as input and return 
# the number of total number of leaves in the tree. The code
# must count the leaves by traversing the tree.
#
#############################################################

#Binary Tree class from Lecture 3 Slides
#with helper functions
class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None
        
    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.left_child = self.left_child
            self.left_child = new_child
    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.right_child = self.right_child
            self.right_child = new_child
    def get_root_val(self):
        return self.key
    def set_root_val(self, new_obj):
        self.key = new_obj
    def get_left_child(self):
        return self.left_child
    def get_right_child(self):
        return self.right_child
    
#added a function to check if a node is a leaf or not
    def is_leaf(self):
        if (self.right_child==None and self.left_child==None):
            return True
        else:
            return False

#PART A: count total nodes through tree traversal
    def count_nodes(self):
        #checks if current node is a leaf. If so, returns 1 to be added to count.
        if self.is_leaf():
            return 1
        #keeps track of number of nodes and increases each time the function is called
        count =+ 1
        #checks if a child exists. If so, it traverses the subtree by recursively 
        #calling the function. 
        if self.right_child != None:
            count += self.right_child.count_nodes()
        if self.left_child != None:
            count += self.left_child.count_nodes()
        #returns the total sum of nodes
        return count  

#PART B: count leaf nodes through tree traversal    
    def count_leaves(self):
        #checks if current node is a leaf. If so, returns 1 to be added to count.
        if self.is_leaf():
            return 1
        count = 0
        #checks if a child exists. If so, it traverses the subtree by recursively 
        #calling the function. 
        if self.right_child != None:
            #adds total leaves of right child to count
            count += self.right_child.count_leaves()
        if self.left_child != None:
            #adds total of leaves of left child to count
            count += self.left_child.count_leaves()
        #returns the total number of leaves
        return count    
        


#Create a Test Binary Tree
a_tree = BinaryTree("a")
a_tree.insert_left("b")
a_tree.insert_right("c")
a_tree.get_left_child().insert_left("d")
a_tree.get_left_child().insert_right("e")
a_tree.get_right_child().insert_left("f")
a_tree.get_right_child().insert_right("g")
a_tree.get_right_child().get_right_child().insert_left("h")
a_tree.get_right_child().get_right_child().insert_right("i")
'''
tree looks like:
#######(a)##########
######/###\#########
####(b)###(c)#######
###/#\#####/#\######
#(d)#(e)#(f)#(g)####
#############/\#####
##########(h)#(i)###
'''

#---Test-Code---
#can comment out nodes(like d,e,f,h,i) to test the function 

#calls the count_nodes() function for the Binary Tree a_tree
print("Number of Total Nodes:", a_tree.count_nodes()) 
#calls the count_leaves() function for the Binary Tree a_tree
print("Number of Leaf Nodes:", a_tree.count_leaves())





