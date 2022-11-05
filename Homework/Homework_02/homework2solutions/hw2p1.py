# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 21:39:00 2021

@author: Swamy
Homework 2 - Q 1, 2
"""

from node import Node

class CharList:
    
    def __init__(self):
        self.lchar = []  #python list of chars
        self.llchar = None #linked list of chars
        self.nchars = 0
        
    def str2pylist(self, data):
        
        for c in data:
            self.lchar.append(c)
    
    def str2ll(self, data): #linked list
        
        if(data):
            
            self.llchar = Node(data[0])
            
            for j in range(1, len(data)):
                temp = Node(data[j])
                temp.set_next(self.llchar)
                self.llchar = temp
    
    def ll_len(self):
        
        temp = self.llchar
        
        while(temp):
            self.nchars += 1
            temp = temp.get_next()
        
        return self.nchars
    
    def printpylist(self):
        print(self.lchar)
        
    def printllchar(self):
        temp = self.llchar
        
        while(temp):
            print(temp.get_data(), end='->')
            temp = temp.get_next()
            
        print('None')
    
    def ispalindrome(self):
            
        nchars = self.ll_len()
        i = 0
        
        while(i < nchars/2):
            
            j = 0
            k = 0
            beginptr = self.llchar
            endptr = self.llchar
            
            #adjust the beginptr through first half of string
            while(j < i and beginptr):
                beginptr = beginptr.get_next()
                j += 1
                
            #adjust the endptr to the end and scan through second half
            while(k < nchars - 1 - i and endptr):
                endptr = endptr.get_next()
                k += 1
    
            if(beginptr.get_data() != endptr.get_data()):
                print("Not palindrome")
                return

            i += 1
        
        print("Palindrome")
             
#########################################
#main code

cobj = CharList()

# cobj.str2pylist('hello')
# cobj.printpylist()
cobj.str2ll('xyzfzyx')
cobj.printllchar()
cobj.ispalindrome()
