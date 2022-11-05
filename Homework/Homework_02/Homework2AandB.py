# -*- coding: utf-8 -*-
#############################################################
# Homework 2 Problem a and b
# author: Craig Shaffer
# date revision: 9/15/21
# course: CPSC 330
#
# a. code for a CharList class which converts a string to a 
# linked list of characters in the string. uses helper 
# function convert_str to convert a string to Linked List
#
# b. add a class member function which outputs if the linked 
# list in Problem a. is a palindrome. Upper bound on PDF
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
#create CharList class with helper functions
class CharList:
    def __init__(self):
        self.head = None   
    def is_empty(self):
        return self.head == None
    #used to add nodes to linked list
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp  
    #prints the linked list
    def print_list(self):
        temp = self.head
        while(temp):
            temp.print_node()
            temp = temp.get_next()
#Part A: convert string to linked list
    def convert_str(self, string):
        #iterates through string and adds characters as nodes to linked list
        for i in range(len(string)):
            self.add(string[i])
#Part B: check palindrome
    def is_palindrome(self):
        temp = self.head
        compList = [] #regular array to compare with values in linked list
        palindrome = True #initialize true, if false then not palindrome        
        #loop adds node into array for comparison
        while temp:
            compList.append(temp.get_data()) #append -> add to array
            temp = temp.get_next() #temp goes to next item         
        temp = self.head
        #iterate through the array, check if the array value i = the value in the LinkList
        for i in compList[::-1]:
            # If not the same, palindrome = False. Therefore, not a palindrome
            if i != temp.get_data(): 
                palindrome = False
            temp = temp.get_next() 
        return palindrome #returns true if it is a palindrome, false if not


#Not a Palindrome Example
string1 = "craig"
#convert to linked list and print
linkedList1 = CharList()
linkedList1.convert_str(string1)
linkedList1.print_list()
#palindrome test
print("Is it a palindrome?")
print(linkedList1.is_palindrome())
print("--------------")

#Palindrome Example
string2 = "racecar"
#convert to linked list and print
linkedList2 = CharList()
linkedList2.convert_str(string2)
linkedList2.print_list()
#palindrome test
print("Is it a palindrome?")
print(linkedList2.is_palindrome())
print("--------------")


