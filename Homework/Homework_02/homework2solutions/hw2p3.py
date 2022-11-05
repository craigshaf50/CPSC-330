# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 10:42:39 2021

@author: Swamy
Homework 3 - Q3
Doubly linked list node
Homework 3, Q4 ???
"""

from dnode import DNode

class DCharList:
    
    def __init__(self):
        self.llchar_head = None #linked list of chars
        self.llchar_tail = None #linked list of chars
        self.nchars = 0
    
    def str2ll(self, data): #linked list
        
        if(data):
            
            self.llchar_head = DNode(data[0])
            self.llchar_tail = self.llchar_head
            
            for j in range(1, len(data)):
                temp = DNode(data[j])
                temp.set_next(self.llchar_head)
                self.llchar_head.set_prev(temp)
                self.llchar_head = temp
                
    def printforward(self):
        temp = self.llchar_head
        
        while(temp):
            print(temp.get_data(), end='->')
            temp = temp.get_next()
            
        print('None')
    
    def printreverse(self):
        temp = self.llchar_tail
        
        while(temp):
            print(temp.get_data(), end='->')
            temp = temp.get_prev()
            
        print('None')
    
    def ispalindrome(self):
        
        begin = self.llchar_head
        end = self.llchar_tail
        
        while(begin != end):
         
            if(begin.get_data() != end.get_data()):
                print('Not palindrome')
                return
            begin = begin.get_next()
            end = end.get_prev()
            
        print('palindrome')
        
#########################################
#main code

cobj = DCharList()

# cobj.str2pylist('hello')
# cobj.printpylist()
cobj.str2ll('xyzfzyx')
cobj.printforward()
cobj.printreverse()
cobj.ispalindrome()