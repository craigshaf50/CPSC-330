# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:13:57 2021

@author: Swamy
"""
#homework 3 solutions
#code by swamy ponpandi
#cpsc 330 fall 2021

from treenode import TreeNode

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def get_root(self):
        return self.root
     
    def set_root(self, r):
        self.root = r
        
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
    
    def postorder_print(self, node):
       
       if(node):
          self.postorder_print(node.get_left_child())
          self.postorder_print(node.get_right_child())
          print(node.get_key(), end= ' ') 
          
    #homework3 - Q1     
    #total num nodes using post order
    def num_nodes_postorder(self):

        return self._post_order(self.root)
    
    def _post_order(self, cur_node):

      if(not cur_node):
          return 0
      
      if(cur_node.is_leaf()):
           return 1
      else:
           l = self._post_order(cur_node.left_child)
           r = self._post_order(cur_node.right_child)
           return (l + r + 1)
        
    #homework 3 - Q2    
    #total num leaves using postorder
    def nleaves(self, cur_node):
     
      if(not cur_node):
          return 0
      
      if(cur_node.is_leaf()):
           return 1
      else:
           l = self.nleaves(cur_node.left_child)
           r = self.nleaves(cur_node.right_child)
           return (l + r)

    #homework 3 - Q4
    #find the leftmost node that has no left child (say node A) following 
    #the left child links starting from the right child of the node to be
    #deleted
    #why ? everything to right of node A is greater than the key of node A
    def find_leftmost_node(self, node_to_be_deleted):
       #assuming node_to_be_deleted has two children
    
       rchild = node_to_be_deleted.get_right_child()
       while(rchild.get_left_child()):
          rchild = rchild.get_left_child()
       
       return rchild
     
    def delete_node_2children(self, node):
        
        #get leftmost node in right subtree of node to be
        #deleted
        leftmost_node = self.find_leftmost_node(node)
        
        #make root of left subtree of node to be deleted to be 
        #child of left child of 'leftmost_node' found above
        lchild_of_node_tobe_deleted = node.get_left_child()
        
        leftmost_node.set_left_child(lchild_of_node_tobe_deleted)
        lchild_of_node_tobe_deleted.set_parent(leftmost_node)
        
        #set the parent of right child of node to be deleted to
        #point to the parent of node to be deleted
        rchild_of_node_tobe_deleted = node.get_right_child()
        
        if(node == self.get_root()): #node to be deleted is root
           node.set_left_child(None) #garbage collection
           node.set_right_child(None)
           self.set_root(rchild_of_node_tobe_deleted)
           rchild_of_node_tobe_deleted.set_parent(None)
           return 
        #node is an internal node
        parent_of_node_tobe_deleted = node.get_parent()
        
        rchild_of_node_tobe_deleted.set_parent( \
                                               parent_of_node_tobe_deleted)
        
        if(node.is_left_child()):
           parent_of_node_tobe_deleted.set_left_child(rchild_of_node_tobe_deleted)
        else:
           parent_of_node_tobe_deleted.set_right_child(rchild_of_node_tobe_deleted)
        
        node.set_left_child(None)
        node.set_right_child(None)
        
bst = BinarySearchTree()

bst.put(4, 2)
bst.put(13, 3)
bst.put(41, 12)
bst.put(3, 6)
bst.put(24, -5)
bst.put(-3, 23)
bst.put(22, -5)
bst.put(49, -5)
bst.put(43, -5)
bst.put(55, -5)

print('num of nodes ', bst.num_nodes_postorder())

#print(bst.get(41))

#Q1 test case
#print(bst.num_nodes_postorder())
#Q2 test case
#print(bst.nleaves(bst.get_root()))

#Q4 test case - internal node
node_delete = bst._get(41,bst.get_root())
#print(node_delete.get_key())
leftmost_node = bst.find_leftmost_node(node_delete)
#print(leftmost_node.get_key())
bst.delete_node_2children(node_delete)
bst.postorder_print(bst.get_root())

#Q4 test case - delete the root
# bst.postorder_print(bst.get_root())

# node_delete = bst.get_root()
# #print(node_delete.get_key())
# leftmost_node = bst.find_leftmost_node(node_delete)

# #print(leftmost_node.get_key())

# bst.delete_node_2children(node_delete)
# #print('num of nodes ', bst.num_nodes_postorder())  
# print('')
# bst.postorder_print(bst.get_root())



