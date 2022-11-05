# -*- coding: utf-8 -*-
####################################################
# Class Activity
# author: Craig Shaffer
# date revision: 9/3/21
# course: CPSC 330
#
# Optimizing Bubble Sort - including a method to
# check if swaps occured. If no swaps in inner loop,
# then the algorithm stops.
#
# input - a list
# output - the sorted list
#
####################################################

#optimized bubble sort
def bubble_sort_opt(a_list):
    #traverse through all in the list
    for i in range(len(a_list) - 1):
        exchange=False
        #last i elements are already in place
        for j in range(len(a_list) - 1 - i):
            #traverse the list from 0 to (n-i)-1. Swap if the element found > next element
            if a_list[j] > a_list[j + 1]:
                temp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = temp
                exchange = True #notes that a swap occured in the iteration
        #If no swaps in the iteration, break     
        if(exchange == False):
            break
    return a_list

#test
list1 = [108, 12, 20, 13, 76, 9, 45]
print(bubble_sort_opt(list1))