"""
A function that takes two lists of numbers and returns the result of merging 
the lists. The elements of the first list should become the elements at the 
even indexes of the returned list, while the elements of the second list should 
become the elements at the odd indexes.
"""

# START
# Given 2 equal length lists of numbers 

# SET iterator = 1
# SET new_list = empty list

# WHILE iterator <= length of list1
# SET list1_number = list 1 number at position iterator
# SET list2_number = list 2 number at position iterator
# SET new_list = new_list + list1_number 
# SET new_list = new_list + list2_number
# SET iterator = iterator + 1

# PRINT new_list

def merge(list1,list2):
    iterator = 0
    new_list = []

    while iterator < len(list1):
        list1_num = list1[iterator]
        list2_num = list2[iterator]
        new_list.append(list1_num)
        new_list.append(list2_num)
        iterator += 1
    
    print(new_list)

merge([1,3,5],[2,4,6])