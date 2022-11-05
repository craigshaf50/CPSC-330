# -*- coding: utf-8 -*-
#############################################################
# Homework 2 Problem d and e
# author: Craig Shaffer
# date revision: 9/17/21
# course: CPSC 330
#
# d. add reverse function
#
# e. code to delete item in middle of linked list
#
#############################################################

#Node class from Blackboard
class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
    def get_data(self):
        """Get node data"""
        return self.data
    def set_data(self, node_data):
        """Set node data"""
        self.data = node_data
    def get_next(self):
        """Get next node"""
        return self.next
    def set_next(self, node_next):
        """Set next node"""
        self.next = node_next
    def print_node(self):
        """String"""
        print('Node: ', self.data)
#List class from Blackboard
class List:
    def __init__(self):
        self.head = None        
    def is_empty(self):
        return self.head == None    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    def print_list(self):
        temp = self.head        
        while(temp):
            temp.print_node()
            temp = temp.get_next()
    
#Part D: add a reverse function to List class
    #reverses the list by changing links between nodes, thus reversing the list
    #the reverse function
    def reverse_LL(self):
        previous = None
        current = self.head        
        while (current != None):
            nextVal = current.next
            current.next = previous
            previous = current
            current = nextVal            
        self.head = previous
        
#Part E: delete a node in the linked list code
    #deletes the node from linked list by the value
    def delete_mid(self,val):
        #head node store in temp variable
        temp = self.head
        #head node is the node to delete
        if (temp == None):
            if (temp.data != val):
                self.head = temp.next
                temp = None
                return 
        #iterates through link list to find the node to be deleted
        while(temp != None):
            if temp.data == val:
                break
            previous = temp
            temp = temp.next 
        #if node/val not in linked list
        if(temp == None):
            return
        #unlink the node from linked list, connect the previous node and the next node 
        previous.next = temp.next 
        temp = None


    
#-----test code-----
ll = List()
#add nodes to list
ll.add(8)
ll.add(31)
ll.add(48)
ll.add(53)
print("Original List:")
ll.print_list()
ll.reverse_LL()
print("Reversed List:")
ll.print_list()
print("Delete test:")
ll.delete_mid(31)
ll.print_list()
print("Delete test:")
ll.delete_mid(53)
ll.print_list()
