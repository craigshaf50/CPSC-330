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
    def size(self):
        temp = self.head
        count = 0        
        while(temp):
            count +=1 
            temp = temp.get_next()           
        return count    
    def search(self, val):       
        temp = self.head        
        while(temp):
            if(temp.get_data() == val):
                return True
            temp = temp.get_next()            
        return False    
    def delete_node(self, val):       
        #list is empty
        if(self.head == None):
            print('List is empty')
            return        
        temp = self.head       
        #one item in the list
        if(temp.get_next() == None):
            if(temp.get_data() == val):
                self.head = None
            return      
        #delete first item
        if(temp.get_data() == val):
            self.head = temp.get_next()
            return        
        temp_prv = self.head #previous pointer
        temp_cur = temp_prv.get_next() #current pointer        
        while(temp_cur):            
            if(temp_cur.get_data() == val):
                temp_prv.set_next(temp_cur.get_next())
            temp_prv = temp_prv.get_next()
            temp_cur = temp_cur.get_next()
            
# ll = List()

# ll.add(5)
# ll.add(12)
# ll.add(7)
# ll.add(-1)
# ll.add(2)

# print(ll.size())
# ll.print_list()
# print(ll.search(5))

# ll.delete_node(12)
# ll.print_list()