'''
* Create a function that is given a list of 5 different numbers as a parameter.
* Sort this list in any way other than using methods from the List object. That means no calling the ".sort()" or "sorterd()" method.

'''

numbers = [8, 3, 5, 9, 1]           # Hardcoded list
lenNums = len(numbers)              # assigning the list items length to a variable
newList = []                        # creating an empty List to save the sorted List
def difNums(nums):              
    i = 0                           # setting initial value as 0

    while(i < lenNums):             
        minVal = min(numbers)       # finding the minimun value in the "numbers List"
        newList.append(minVal)      # appending that value to the "newList"
        numbers.remove(minVal)      # removing that value from the original List
        i += 1                      # increment

    print(newList)                  # display the newList on the CLI
 

difNums(numbers)                    # passing the "numbers List" through the function given
