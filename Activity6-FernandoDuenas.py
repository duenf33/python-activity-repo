'''
Activity 6: Dictionaries
* Create an activity file.
'''
# In this file I want you to create a Dictionary named "car".
# The car has a brand, a model, and year.

car = {
    "brand": "ford",
    "model": "mustang",
    "year": "1964"
}

print(car['model'])

'''
Perform Dictionary Methods on your Object, and in a comment explain the result you expected vs the result that you got.
'''

# i expect to get an empty Dictionany.
# print(car.clear())
# print(car)

# This on is only making a reference to the original
car2 = car
print('original:', car)
print('car2 copy:', car2)

# Using the copy() method a new dictionary is created, having a copy of the references from the original.
carCopy = car.copy()
print('carCopy: ', carCopy)