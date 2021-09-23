'''
* Create a function that is given a list of 5 different numbers as a parameter.
* Sort this list in any way other than using methods from the List object. That means no calling the ".sort()" or "sorterd()" method.

'''

numbers = [8, 3, 5, 9, 1]
lenNums = len(numbers)
newList = []
def difNums(nums):
    i = 0

    while(i < lenNums):
        minVal = min(numbers)
        newList.append(minVal)
        numbers.remove(minVal)
        i += 1

    print(newList)
 

difNums(numbers)
