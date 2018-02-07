import math

"""
Robert Matthews
CS 1400
Section 002
Exercise 3

3.1
Chapter 3, Discussion #2, pg. 78. Translate each of the expressions given in the problem into Python code. Execute each
expression in the shell, using reasonable input values where necessary. Make a session record of your interactions with
the shell (save the interaction to a file) and submit it as your answer.
"""

'''
Translate each of the following mathematical expressions into an equivalent Python expression. You may assume that the 
math library has been imported (via import math).
'''


def calculate_expression_d(a, b, y):
    first_half = y * (math.cos(a) ** 2)
    second_half = y * (math.sin(b) ** 2)
    result = math.sqrt(first_half + second_half)
    return result


print(str(math.factorial(100)))

print("This program will calculate all 5 expressions from Chapter 3, Discussion 2")
print("User input will be required for expression b, c, d, and e")


# a) (3 + 4)(5)

# expressionA = (3 + 4)*5
# print("expression A:", expressionA)
#
# # b) (n(n - 1))/2
# variableB1 = eval(input("Enter the value for the variable in expression B: "))
# expressionB = (variableB1 * (variableB1 - 1))/2
# print("expression B:", expressionB)
#
# # c) 4*pi*r^2
# variableC1 = eval(input("Enter the value for the radius in expression C: "))
# expressionC = 4*math.pi*(variableC1*variableC1)
# print("expression C:", expressionC)

# d) (y(cos a)^2 + y(sin b)^2)^(1/2)
variableD1 = eval(input("Enter the first variable in expression D: "))
variableD2 = eval(input("Enter the second variable assigned to the cos function in expression D: "))
variableD3 = eval(input("Enter the third variable assigned to the sin function in expression D: "))

expressionD = calculate_expression_d(variableD2, variableD3, variableD1)
# expressionD = math.sqrt(variableD1(math.cos(variableD2)**2) + variableD1(math.cos(variableD2)**2))
print("expression D:", expressionD)

# e) (y2 - y1)/(x2 - x1)
variableE1 = eval(input("Enter the value for the first x coordinate in expression E: "))
variableE2 = eval(input("Enter the value for the first y coordinate in expression E: "))
variableE3 = eval(input("Enter the value for the second x coordinate in expression E: "))
variableE4 = eval(input("Enter the value for the second y coordinate in expression E: "))
expressionE = (variableE4 - variableE2)/(variableE3 - variableE1)
print("expression E:", expressionE)
