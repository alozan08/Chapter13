# Complete the function that takes an integer as input and returns the factorial of that integer

# from math import factorial
# def calculate(x):
#     return factorial(x)
#
#
# print(calculate(3))  # expected outcome: 6
# print(calculate(9))  # expected outcome: 362880


########################################################################################################################
# Complete the function that takes a list as input and returns a randomized item from that list

# import random as r
# def selection(x):
#     return r.choices(x, k=1)
#
#
# print(selection(['apple', 'banana', 'orange', 'grape']))
# print(selection([7, 5, 3, 9, 12, 4, 8, 10]))


########################################################################################################################
# Complete the function that takes as input an integer for a number of days and prints the total number of seconds
# in that number of days

# import datetime
#
# def currentDate(x):
#     seconds =  datetime.timedelta(days=x).total_seconds()
#     print(f'The total number of seconds is {seconds}')
#
#
# currentDate(4)  # expected outcome: The total number of seconds is 345600.0.
# currentDate(7)  # expected outcome: The total number of seconds is 604800.0.


########################################################################################################################

import datetime as dt

def currentDate():
    today = dt.date.today()
    return today.strftime("%m-%d-%Y")

print(currentDate())  # Expected outcome will vary, but should follow this format: The current date is 9-11-2018.

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################