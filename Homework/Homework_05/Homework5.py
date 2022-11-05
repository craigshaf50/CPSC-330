# -*- coding: utf-8 -*-
#################################################################
# Homework 5 A and B
# author: Craig Shaffer
# date revision: 12/1/21
# course: CPSC 330
#
# a. Implement your own dictionary class, using hash table with 
# open hashing collision resolution, for O(1) (average) search,
# insertion and deletion. Assume the key, value pairs are 
# string data type. Use any appropriate hash function. 
#
# b. Determine the experimental efficiency (average case 
# performance) of your dictionary in problem a. using the sample
# text files provided. You will need to read the files in Python 
# using file operations, extract the words (read line by line 
# and split the string into individual words), insert the words 
# into the dictionary. The value part of key-value pair can be 
# empty for this experiment. You must keep track of how long it
# takes to insert each word. There is no deletion in this 
# experiment. Tabulate the average time taken for insertion in
# each hash table location. Use the data to compute the overall
# performance of your dictionary.
#################################################################

#Modified Node class to include tuple for the dictionary key and value
#includes print_node and get_next functions
class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None
    #prints the key/value pair of the dictionary entry (node)
    def print_node(self):
        print('Dictionary Entry: ', self.pair)
    #gets next node in linked list
    def get_next(self):
        return self.next

#Dictionary class
class MyDictionary:
#hash of desired size, entries initialized to None
#added self.entries and self.count for determining experimental efficiency
#self.entries will count how many entries are present in the hash
#self.count will be used to store the sum of time to reach a node 
#It will be divided by hash slots to be used to find experimental efficiency
    def __init__(self,size):
        self.size = size
        self.h = [None]*self.size
        self.entries = 0
        self.count = 0
#get size funtion from template
    def getsz(self):
        return self.sz
#hash function to return the index in which a given string will be stored
#gives each key(mstr) an index by summing the ordinal values of the characters
#then returns sum mod the size 
    def hashFunction(self, mstr):
        sum = 0
        for char in range(len(mstr)):
            sum = sum + ord(mstr[char])
        return sum % self.size
    
#adds given string(key) to the hash
#first if statement checks if a string exists in the hash slot
#if one does not exist it adds the key to the hash
#if one does exist then it checks if the key is already present, 
#if it is not then it adds it to the linked list
#---- also updates self.count and self.entries - (used for experimental efficiency in part B) 
    #updates self.entries by 1 when adding a node to the linked list
    #updates the self.count by how long it would take to get to the added node
    # ex- node is first in a linked list, it would take 1 time. node is second, it would take 2 time. And so on
    def addtoHash(self, mstr, value):
        key = mstr
        index = self.hashFunction(mstr)
        counter=1 #used to keep track of what position a node is added to, used to update self.count
        if self.h[index] == None:
            self.h[index] = ListNode(key, value)
            self.entries = self.entries + 1
            self.count = self.count + counter
        else:
            cur = self.h[index] #cur is first node in linked list
            while True:
                if self.isInHash(mstr) == True:
                    return
                if cur.next == None: 
                    break
                counter=counter + 1 #update counter to the next position
                cur = cur.next 
            cur.next = ListNode(key, value) 
            self.entries = self.entries + 1
            self.count = self.count + counter
            
#prints the hash contents to see if everything is working well
#iterates through hash indices to determine if an entry is present
#if one is then it will print the nodes in the linked list at that index
#and continue this process to the end of the hash
    def printHash(self):
        i=0
        while i < self.size:
            if self.h[i] != None:
                temp = self.h[i]
                print('Index:', i)
                while(temp):
                    temp.print_node()
                    temp = temp.get_next()
            i= i+1
        return
    
#check if a given string(key) is in hash or not
#checks if the string matches the key of a node in linked list at the 
#index it should be in
    def isInHash(self, mstr):
        index = self.hashFunction(mstr)
        cur = self.h[index]
        while cur:
            if cur.pair[0] == mstr:
                return True
            else:
                cur = cur.next
        return False
    
#delete a key from the hash, if it exists
#finds index of key and checks if key exits
#removes node by "unlinking" it from the list
    def delHash(self, mstr):
        index = self.hashFunction(mstr)
        cur = prev = self.h[index] #initialize cur and prev to first node
        if not cur: 
            return
        if cur.pair[0] == mstr:
            self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == mstr:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next
               
#additional helper function that returns the value attached to the key. 
#for the text file testing the values will be set to an empty string ''
    def getVal(self, mstr):
        index = self.hashFunction(mstr)
        cur = self.h[index]
        while cur:
            if cur.pair[0] == mstr:
                return cur.pair[1] #returns the 'value' slot of the tuple self.pair
            else:
                cur = cur.next
        return "The key does not exist, therefore there is no value to return"

#prints the experimental efficiency, used for part B
    def printExpEff(self):
        expEff = self.count / self.entries
        print("Experimental Efficiency (time/key) =", expEff, "time units per key on an average")

#returns the number of entries, can be used to get the number of entries in the dictionary
    def numEntries(self):
        return self.entries

# ----------PART A----------
###### test code for the functions above ######
#uncomment what you wish to test, feel free change size of test dictionary

#create dictionary
# dict1 = MyDictionary(15)

#build test hash dictionary
# dict1.addtoHash('cragi','object1')
# dict1.addtoHash('craig','object2')
# dict1.addtoHash('rciag','object3')
# dict1.addtoHash('hippo','object4')
# dict1.addtoHash('ophip','object5')
# dict1.addtoHash('monkey','object6')
# dict1.addtoHash('human','object7')

#test print hash
# dict1.printHash()

#testing deletion (deletes 'craig' from dictionary)
# print('---objects in the dictionary pre deletion---')
# dict1.printHash()
# dict1.delHash('craig')
# print('---objects in the dictionary post deletion---')
# dict1.printHash()

#test isInHash function
# print(dict1.isInHash('rciag')) #should return True
# print(dict1.isInHash('beans')) #should return False

#test printExpEff
# dict1.printExpEff()

#test numEntries
# dict1.numEntries()



# ----------PART B----------
###### test code for adding words from file to dictionary ######
# will print experimental efficiency (time per key on an average)

#create a dictionary object
dict = MyDictionary(1459)

#open the large or small file. file MUST be in the same
#directory as this code file
#srcfile = open('largefile-text.txt','r',encoding='utf8')

srcfile = open('small-file.txt','r',encoding='utf8')

#read each line
for line in srcfile:
    #split each line into strings
    wordlist = line.split()
    if(wordlist):
        #print(wordlist)
        #add each string into the hash
        for mstr in wordlist:
            dict.addtoHash(mstr,'')

#prints the hash
dict.printHash()   

#prints the experimental efficiency of hash function
#for small text file - 1.0236686390532543 time units per key on an average
#for large text file - 6.228965112870126 time units per key on an average
dict.printExpEff()