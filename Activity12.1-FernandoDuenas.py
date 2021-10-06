'''So your task is to, write a function that given a list of exam grades represented by integers, to calculate the standard deviation of the exam grades, and return to me the list with all the exam values updated by itself plus the standard deviation. I want you to include something that states that if adding the standard deviation to the current exam score goes above 100, then I will simply pass in 100 to the list at that particular value, for everything else, just add the standard deviation normally to the current exam score.'''

import statistics

# examGrades = [65, 80, 55, 73, 90, 75]
# # examGrades = [100, 90, 100, 90, 90, 100]
# calc = statistics.stdev(examGrades)
# hCalc = statistics.median_high(examGrades)
# print(hCalc)    # this is printing the median high.

# # I am trying to use this as a helper function to run inside func() function.
# def calcFunc():        
#     # here I am trying to find out how to sum up calc + hcalc and run a for loop to make a conditional if any value in there is higher than 100 to display 100.

#     for i in examGrades:
#         if examGrades[i] > 100:
#             return 100

# def func(elem):

#     return f"these are the list of grades: {elem} and this is the standard deviation: {calc}"
        

# print(func(examGrades))

# -------------------------------------
'''Class solution:'''

def curvedGrades(data1 = [33, 33, 50, 50, 65, 65, 80, 80, 95, 95, 100]):
    stDev = statistics.stdev(data1)
    print(f"\nOriginal Grades:\n{data1}\n")
    print(f"\nStandard Deviation is:\n{stDev}\n")

    for i in range(len(data1)):
        if(data1[i] + int(stDev) > 100):
            data1[i] = 100
        else:
            data1[i] += int(stDev)
            # data1[i] = data1[i] + int(stDev) -> is the same result as above.
    print(f"Curved Grades: {data1}")
    return data1

curvedValues = curvedGrades()
curvedValues

def averageCurved(dataset = [90, 54, 67]):
    curvedGradeList = curvedGrades(dataset)
    meanOfCurved = statistics.mean(curvedGradeList)
    print(f"\nFor your convinience, this is what will be printed out as a result in a new line below:\n{meanOfCurved}\n")
    return meanOfCurved

averageCurved(curvedGrades())

'''from elvis class solution: '''

#Activity X.1
#So your task is to, given a list of exam grades represented by integers, to calculate the standard 
#deviation of the exam grades, and return to me the list with all the exam values updated by itself plus
#the standard deviation. I want you to include something that states that if adding the standard 
#deviation to the current exam score goes above 100, then I will simply pass in 100 to the list at that
#particular value, for everything else, just add the standard deviation normally to the current exam score.

#Solution
    #Working on: data = [1,3,5, 9, 87, 58, 39, 3]
def curvedGrades(data1):
    stDev = statistics.stdev(data1)
    #print(f"This is the original list before modifications: \n {data1}")
    #print(f"\nOriginal Grades:\n{data1}\n")
    for i in range(len(data1)):
        if(data1[i] + int(stDev) > 100):
            data[i] = 100
        else:
            data1[i] += int(stDev)
   
    #print(f"For your convinience here is a printed copy of your list in a new line that is being returned:\n {data1}")
    #print(f"\nCurved Grades:\n{data1}\n")
    return data1

#I can save the value of my function in a variable to use with other functions if needed...
#curvedValues = curvedGrades(data)

#curvedValues


#Activity X.2
#Now I would like you to write a function that returns to me the average value of the curved exam grades
#Create a second function that gets me the average value of the original exam grades:

#Solution
    #Working with: [1,3,5, 9, 87, 58, 39, 3]
def averageCurved(dataset = [1,3,5, 9, 87, 58, 39, 3]):
    # print(f"This is the original list: {dataset}")
    # print(f"The regular average is: {statistics.mean(dataset)}")
    curvedGradeList = curvedGrades(dataset)
    
    #print(f"The curved list of grades is: {curvedGradeList}")
    meanOfCurved = statistics.mean(curvedGradeList)
    print(f"\nFor your convinience, this is what will be printed out as a result in a new line below:\n{meanOfCurved}\n")
    return meanOfCurved

averageCurved(curvedGrades(data))


#Activity X.3
#Get me the mean of the original data list in a function please

#Solution
def averageNormal(dataset):
    #return statistics.mean(dataset)
     mean = statistics.mean(dataset)
     print(f"\n The Mean is:\n{mean}\n")
     return mean

averageNormal(data)
averageCurved(data)