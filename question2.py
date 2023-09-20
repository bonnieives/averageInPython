
"""

    ASSIGNMENT #1
    QUESTION 2
    AUTHOR: Bonnie Ives de Castro Nunes
    DATE: September 15th, 2023
    
"""


print("Please inform the first number: ")
firstNumber = input()
print("------------------------------")

print("\nPlease inform the second number: ")
secondNumber = input()
print("------------------------------")

print("\nPlease inform the third number: ")
thirdNumber = input()
print("------------------------------")

print("\nPlease inform the fourth number: ")
fourthNumber = input()
print("------------------------------")

print("\nPlease inform the fifth number: ")
fifthNumber = input()
print("------------------------------")

print("\n------ Informed Numbers ------")
print("First number informed: " + firstNumber)
print("Second number informed: " + secondNumber)
print("Third number informed: " + thirdNumber)
print("Fourth number informed: " + fourthNumber)
print("Fifth number informed: " + fifthNumber)
print("------------------------------")

summing = int(firstNumber) + int(secondNumber) + int(thirdNumber) + int(fourthNumber) + int(fifthNumber)
average = summing / 5

print("\n\nThe average between the informed numbers is: " + str(average))
