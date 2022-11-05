# -*- coding: utf-8 -*-
#############################################################
# Homework 2 Problem a and b
# author: Craig Shaffer
# date revision: 9/17/21
# course: CPSC 330
#
# a. code for a CharList class which converts a string to a 
# linked list of characters in the string
#
# b. add a class member function which outputs if the linked 
# list in Problem a. is a palindrome. Upper bound on PDF
#
#############################################################

#Class for CharList with helper functions to convert a string to a Linked List     
class CharList:
    def __init__(self):
        self.data = None
        self.next = None
        self.head = None
    
    #makes new node for the CharList to add to linked list
    def add(data): 
        newNode = CharList()
        newNode.data = data
        newNode.next = None
        return newNode
    
    #converts the string to a linked list
    def string_to_LL(string): 
        head = CharList.add(string[0])
        currentNode = head
        # curr pointer points to the current node
        # where the insertion should take place
        for i in range(len(string) - 1):   
            currentNode.next = CharList.add(string[i + 1])
            currentNode = currentNode.next     
        return head
    #prints the list with -> to separate nodes
    def print_(head):
        currentNode = head
        while (currentNode!=None):
            print((currentNode.data), "->")
            currentNode = currentNode.next
#Part B: check if palindrome with is_palindrome
    #no reason to convert item to linked list to check if the string form is
    #the same characters in the same order, therefore, you can just reverse the
    #string in rreverse recursively and check if the reversed string is the same
    #as the original string
    def rreverse(string):
        if string == "":
            return string
        else:
            return CharList.rreverse(string[1:]) + string[0]
    
    #checks if original string is the same as the reversed string    
    def is_palindrome(string):
        if (string == CharList.rreverse(string)):
            print("linked list is a palindrome")
        else:
            print("linked list is not a palindrome")
        
    
       

string1 = "Craig"
string2= 'racecar'
#call to print linked list of string1
CharList.print_(CharList.string_to_LL(string1))
#call to check if palindrome
CharList.print_(CharList.is_palindrome(string1))

#call to print linked list of string2
CharList.print_(CharList.string_to_LL(string2))
#call to check if palindrome
CharList.print_(CharList.is_palindrome(string2))


        
