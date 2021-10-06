#Activity X.3
#Get me the mean of the original data list in a function please

#Solution
'''
def averageNormal(dataset):
    #return statistics.mean(dataset)
     mean = statistics.mean(dataset)
     print(f"\n The Mean is:\n{mean}\n")
     return mean

averageNormal(data)
averageCurved(data)'''

# Now I would like to have a function that takes a list and tells me how many people passed the class.
#I would like you to do this given a list.

# 1. Given a list of integers representing exam grades (wether they are curved or not), print a message telling me how many ppl passed or failed the class based on the fact that 55+ is passing and below is failing.

# my intended solution:
'''import statistics

dataSet = [65, 55, 78, 90, 100, 80]

def func2(elem):
    meanCurved = statistics.mean(elem)
    print(f"this is the mean: {meanCurve}")
    print(trueFalse(elem))
    
func2(dataSet)'''

'''Class solution:
Solution for X.5 V1'''
# def classReport(dataset):
#      passingCount = 0
#      failingCount = 0
#      for i in range(len(dataset)): 
#          if(dataset[i] < 55):
#              failingCount += 1
#          else: 
#              passingCount += 1
#      return f"You have {passingCount} passing students and {failingCount} failing students."

# def classReport2(dataset = [33, 45, 55, 65, 65, 77, 85, 90, 100]):
#     #print(f'Original List {dataset}')
#     boolList = passOrFail(dataset)
#     #print(f'Expected Boolean List {boolList}')
#     passing = boolList.count(True)
#     failing = boolList.count(False)
#     return f"You have {passing} passing students and {failing} failing students."

def foo(a = 1, b = 2):
    return a + b
print(foo(b = 4))
