# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 20:40:45 2021

@author: modified by Swamy
"""

class Node:
    """A node of a linked list"""

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

# n1 = Node(5)
# n1.print_node()