# Write a Python program to insert a new item before the second element in an existing array.

from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Insert new value 4 before 3:")
array_num.insert(1, 4)
print("New array: "+str(array_num))
