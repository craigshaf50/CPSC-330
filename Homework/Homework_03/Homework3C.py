# -*- coding: utf-8 -*-
#############################################################
# Homework 3 Problem C
# author: Craig Shaffer
# date revision: 9/31/21
# course: CPSC 330
#
# c. code for building (insertion) a ternary tree. A node 
# (Ternary tree class) in a ternary tree may have at most 3 
# children.
#
#############################################################

#TernaryTree Class modified from BinaryTree in Lec03 Slides
class TernaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None
        self.middle_child = None #add third child (middle child)       
    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = TernaryTree(new_node)
        else:
            new_child = TernaryTree(new_node)
            new_child.left_child = self.left_child
            self.left_child = new_child            
    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = TernaryTree(new_node)
        else:
            new_child = TernaryTree(new_node)
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

#function to create a middle child for a node
        #checks if middle child exists. If not creates a new node.
        #if middle child exists, new_node becomes the middle child
        #and the original child becomes the middle child of new_node
    def insert_mid(self, new_node):
        if self.middle_child == None:
            self.middle_child = TernaryTree(new_node)
        else:
            new_child = TernaryTree(new_node)
            new_child.middle_child = self.middle_child
            self.middle_child = new_child
            
#helper funtion to get the middle_child of a node
    def get_mid_child(self):
        return self.middle_child



#Create a Test Ternary Tree
a_tree = TernaryTree("a")
a_tree.insert_left("b")
a_tree.insert_mid("c")
a_tree.insert_right("d")
a_tree.get_left_child().insert_left("e")
a_tree.get_left_child().insert_mid("f")
a_tree.get_left_child().insert_right("g")
a_tree.get_mid_child().insert_left("h")
a_tree.get_mid_child().insert_mid("i")
a_tree.get_mid_child().insert_right("j")
a_tree.get_right_child().insert_left("k")
a_tree.get_right_child().insert_mid("l")
a_tree.get_right_child().insert_right("m")
'''
tree looks like:
##############(a)################
############/##|##\##############
#########/#####|#####\###########
######/########|########\########
####(b)#######(c)#######(d)######
###/#|#\#####/#|#\#####/#|#\#####
#(e)(f)(g)#(h)(i)(j)#(k)(l)(m)###
'''

#---Test-Code---
print(a_tree.get_root_val()) #should print a
print(a_tree.get_mid_child().get_root_val()) #should print c
print(a_tree.get_mid_child().get_right_child().get_root_val()) #should print j
print(a_tree.get_left_child().get_mid_child().get_root_val()) #should print f








