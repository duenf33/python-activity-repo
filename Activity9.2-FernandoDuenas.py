'''
* Write a function that does what the List.max() method does.
* Your function will given a list of numbers as a parameter and you are to return the greatest value in that list without using the List.max() method.

'''

nums = [6, 4, 1, 7, 9]

def numList(elem):
    newL = 0
    for i in range(0, len(nums)):   # "i" will iterate through the index of the List starting at 0.
        if(elem[i] > newL):         # if the element in the List is larger than the element stored in the variable "newL", then it will run the next block of code. 
            newL = elem[i]          # the element passed to this line of code will be re-assigned to the variable "newL". 
    return newL                     # the variable "newL" value will be returned with the largest number in the list given.
result = numList(nums)  
print(result)