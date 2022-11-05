# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 10:40:21 2021

@author: Swamy
Homework 3 - Q3
Doubly linked list node
"""

class DNode:
    """A node of a linked list"""

    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None
    
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

    def get_prev(self):
        """Get prev node"""
        return self.prev

    def set_prev(self, node_prev):
        """Set next node"""
        self.prev = node_prev
        
    def print_node(self):
        """String"""
        print('Node: ', self.data)

# n1 = Node(5)
# n1.print_node()