# -*- coding: utf-8 -*-
#############################################################
# Homework 4 Problem A
# author: Craig Shaffer
# date revision: 10/15/21
# course: CPSC 330
#
# a. Generates a random integer list of 1000 items (no 
# duplicates) with integers in the range [1, 10000]. Code 
# builds AVL tree for the list and also prints the height of 
# tree and number of rotations required to balance the tree
#
#############################################################

#import random library to use later for list generation
import random 

#modified TreeNode class that includes balance factor and height
class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.balance_factor = 0 #modified treenode to include balance factor
        self.height=1 #modified treenode to include height

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

#modified binary search tree class to AVLSearchTree
class AVLSearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.right_rot = 0
        self.left_rot = 0
        self.treeheight = 0
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()

#modified put to include height updating
    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size = self.size + 1
        self.treeheight = 1 + max(self.get_height(self.root.left_child),
                             self.get_height(self.root.right_child))
#modified _put from AVL slides
    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left_child:
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(
                    key, value, parent=current_node
                )
                self.update_balance(current_node.left_child)
        else:
            if current_node.right_child:
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(
                    key, value, parent=current_node
                )
                self.update_balance(current_node.right_child)
        
#update_balance function from AVL slides
    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1
    
            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

#rotate_left from AVL slides - slightly modified for height and rotation counting
    def rotate_left(self, rotation_root):
        new_root = rotation_root.right_child
        rotation_root.right_child = new_root.left_child
        if new_root.left_child:
            new_root.left_child.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self.root = new_root
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left_child = new_root
            else:
                rotation_root.parent.right_child = new_root
        new_root.left_child = rotation_root
        rotation_root.parent = new_root
        #uses the heights of children to calculate the balance factor
        rotation_root.balance_factor = (self.get_height(rotation_root.left_child) - self.get_height(rotation_root.right_child))     
        new_root.balance_factor = (self.get_height(new_root.left_child) - self.get_height(new_root.right_child))
        #updates the number of left rotations 
        self.left_rot = self.left_rot + 1 
        #updates height of rotated tree nodes
        rotation_root.height = 1 + max(self.get_height(rotation_root.left_child),
                                 self.get_height(rotation_root.right_child))
        new_root.height = 1 + max(self.get_height(new_root.left_child),
                                 self.get_height(new_root.right_child))

#rotate_right derived from rotate_left
    def rotate_right(self, rotation_root):
        new_root = rotation_root.left_child
        rotation_root.left_child = new_root.right_child
        if new_root.right_child:
            new_root.right_child.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self.root = new_root
        else:
            if rotation_root.is_right_child():
                rotation_root.parent.right_child = new_root
            else:
                rotation_root.parent.left_child = new_root
        new_root.right_child = rotation_root
        rotation_root.parent = new_root
        #uses the heights of children to calculate the balance factor
        rotation_root.balance_factor = (self.get_height(rotation_root.left_child) - self.get_height(rotation_root.right_child))     
        new_root.balance_factor = (self.get_height(new_root.left_child) - self.get_height(new_root.right_child))
        #updates the number of right rotations 
        self.right_rot = self.right_rot + 1
        #updates height of rotated tree nodes
        rotation_root.height = 1 + max(self.get_height(rotation_root.left_child),
                                 self.get_height(rotation_root.right_child))
        new_root.height = 1 + max(self.get_height(new_root.left_child),
                                 self.get_height(new_root.right_child))
#rebalance function from AVL slides
    def rebalance(self, node):
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)

    def __setitem__(self, key, value):
        self.put(key, value)
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
    def __getitem__(self, key):
        return self.get(key)

#helper function to get the height of a node
    def get_height(self, node):
        if not node:
            return 0
        else:
            node.height=1+max(self.get_height(node.left_child),
                              self.get_height(node.right_child))
        return node.height



#-----------test-code-----------

#generates random list of integers from 1 to 10000 using the random library
#sample prevents the list from including duplicates
randomList=random.sample(range(1,10000),1000)

#print(randomList)

#create avl tree to fill with values from the randomList
avlTree = AVLSearchTree()


#Build the tree by adding each item from randomList into the AVL tree using while loop
i=0 #initialize index
while i<1000:
    avlTree.put(randomList[i],str(randomList[i]))
    i=i+1


#code to print size, rotations(left and right), total rotations, and height
print("size: tree has",avlTree.size,"nodes")
print("rotations:",avlTree.right_rot, "right rotations and ",avlTree.left_rot,"left rotations" )
print("total rotations:", avlTree.right_rot + avlTree.left_rot)
print("height: tree is", avlTree.treeheight,"tall")
