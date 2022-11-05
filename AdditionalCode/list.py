# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 09:57:18 2021

@author: Swamy
"""
from node import Node

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
        
ll = List()

ll.add(5)
ll.add(12)
ll.add(7)


ll.print_list()