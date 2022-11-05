# -*- coding: utf-8 -*-
#############################################################
# Homework 3 Problem D
# author: Craig Shaffer
# date revision: 9/31/21
# course: CPSC 330
#
# d. code to delete node with two children via alternate 
# method. 
#
#############################################################
#using BinarySeachTree code from lec04 BST slides
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
        
#Deletion from BST slides with the alternative technique added
    def delete_node(self, current_node):
        if (current_node.is_leaf()): #if no children
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None

#PART D: Alternative Technique of Deleting Node with two children
        elif current_node.has_children(): #if two children
            
            #Copies left_child of current_node into the left most child's empty
            #left_child in the right_child of current_node's subtree.
            #then replaces current_node with it's right_child
        
            #store the right_child of current node into temp
            temp=current_node.right_child
            #loop to find left most child of current_node's right_child
            while temp.get_left_child != None:
                temp=temp.left_child
            #copy current_node's left_child into a new node that is a child of the 
            #left most node in the current_node's right_child. Now the left_child's
            #subtree is in the left most part of current_node's right_child
            temp.left_child=TreeNode(current_node.left_child.key,
                                     current_node.left_child.value,
                                     current_node.left_child.left_child,
                                     current_node.left_child.right_child,
                                     temp)
            #Now the left_child's subtree is in the left most part of current_node's right_child
            #so we can replace current_node with it's right_child.
            current_node.replace_value(
                    current_node.right_child.key,
                    current_node.right_child.value,
                    current_node.right_child.left_child,
                    current_node.right_child.right_child)
               
        else: # removing a node with one child from BST slides
            if current_node.get_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_value(
                    current_node.left_child.key,
                    current_node.left_child.value,
                    current_node.left_child.left_child,
                    current_node.left_child.right_child,
                    )
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_value(
                    current_node.right_child.key,
                    current_node.right_child.value,
                    current_node.right_child.left_child,
                    current_node.right_child.right_child)


        
bst = BinarySearchTree()
bst.put(4, 'a')
bst.put(13, 'b')
bst.put(41, 'c')
bst.put(3, 'd')
bst.put(24, 'e')
bst.put(-3, 'f')
bst.put(54, 'g')
bst.put(43, 'h')
bst.put(62, 'i')

'''
deleting 41 'c' with new method
tree looks like before: vs after:
#######(a)############|#######(a)##########
######/###\###########|######/###\#########
####(d)###(b)#########|####(d)###(b)#######
###/#########\########|###/#########\######
#(f)#########(c)######|#(f)#########(g)####
#############/\#######|##############/\####
##########(e)#(g)#####|###########(h)#(i)##
##############/\######|###########/########
###########(h)#(i)####|#########(e)########
'''


print(bst.num_nodes())
print(bst.get(4))
print(bst.get(41))
bst.delete_node(41)

