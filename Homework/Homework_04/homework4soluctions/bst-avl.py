# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:13:57 2021

@author: Swamy
"""
#homework 4 solutions
#code by swamy ponpandi
#cpsc 330 fall 2021

from treenode import TreeNode

class AVLBinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.numrots = 0  #count num rotations
    
    def get_numrots(self):
        return self.numrots
    
    def get_root(self):
        return self.root
     
    def set_root(self, r):
        self.root = r
        
    def num_nodes(self):
        return self.size
    
    
    def avlput(self, key, value):
        if self.root:
            self._avlput(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        
        self.size = self.size + 1
        
    
    def _avlput(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._avlput(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                
                print('key inserted - ', key)
                print('post order before balancing :: ', end = ' ')
                self.postorder_print(self.get_root())
                
                self.updateBalance(currentNode.leftChild)
                
                print('')
                print('post order after balancing :: ', end = ' ')
                self.postorder_print(self.get_root())
                print('')
        else:
            if currentNode.hasRightChild():
                self._avlput(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                
                print('key inserted - ', key)
                print('post order before balancing :: ', end = ' ')
                
                self.postorder_print(self.get_root())
                self.updateBalance(currentNode.rightChild)
                
                print('')
                print('post order after balancing :: ', end = ' ')
                self.postorder_print(self.get_root())
                print('')
                
    def updateBalance(self,node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            #self.postorder_print(self.get_root())
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)     
    
    def rebalance(self,node):
       if node.balanceFactor < 0:
         if node.rightChild.balanceFactor > 0:
            self.rotateRight(node.rightChild)
            self.rotateLeft(node)
            self.numrots += 2
         else:
            self.rotateLeft(node)
            self.numrots += 1
            
       elif node.balanceFactor > 0:
         if node.leftChild.balanceFactor < 0:
            self.rotateLeft(node.leftChild)
            self.rotateRight(node)
            self.numrots += 2
         else:
            self.rotateRight(node)
            self.numrots += 1
            
    
    def rotateLeft(self,rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
                
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self,rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
            
        newRoot.parent = rotRoot.parent
        
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 - max(-rotRoot.balanceFactor, 0)
        
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
            return self._get(key, current_node.leftChild)
        else:
            return self._get(key, current_node.rightChild)
    
    def postorder_print(self, node):
       
       if(node):
          self.postorder_print(node.get_left_child())
          self.postorder_print(node.get_right_child())
          print(node.get_key(), ' ', node.balanceFactor, end= ' ') 
          
   
#driver code to test avl tree
bst = AVLBinarySearchTree()

bst.avlput(4, 2)
bst.avlput(13, 3)
bst.avlput(41, 12)
bst.avlput(3, 6)
bst.avlput(24, -5)
bst.avlput(-3, 23)
bst.avlput(22, -5)
bst.avlput(49, -5)
bst.avlput(43, -5)
bst.avlput(55, -5)

print('num of rotations = ', bst.get_numrots())




