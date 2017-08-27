'''

@author Harold S. Umali

Originally Created in: Febuary 19 2015
Revised in: August 26 2017

Description: If-else statement - Given three inputs, checking and telling if
  there is any pair that would equal to the third number and if the highest
  number among the three is even or odd.

  UPDATED (08/26):
    - added functions for code reusability
    - revised for the sake of practicing variable naming and making functions
      according to the problem domain
    - the goal is to make some parts of the code, if not all, self-documenting
    - 27 LESS READABLE LINES (OLD) vs. 30 MORE READABLE LINES (NEW)

'''

def promptSum(prompt):
    ## C programming style of returning strings with format specifiers
    ## eg.
    ##     printf("%i + %i = %i", secondNum, thirdNum, firstNum);
    ## the part ["%i + %i = %i", secondNum, thirdNum, firstNum] is similar
    ##   to the return values below...
    if (prompt == 1):
        return "{} + {} = {}".format(secondNum, thirdNum, firstNum)
    elif (prompt == 2):
        return "{} + {} = {}".format(thirdNum, firstNum, secondNum)
    elif (prompt == 3):
        return "{} + {} = {}".format(firstNum, secondNum, thirdNum)
    else:
        return "No pair is equal to any number..."

def checkSum(firstNum, secondNum, thirdNum):
    if (firstNum + secondNum == thirdNum):
        print(promptSum(3)) ## call function promptSum(<resultingNumberGiven>)
    elif (secondNum + thirdNum == firstNum):
        print(promptSum(1))
    elif (thirdNum + firstNum == secondNum):
        print(promptSum(2))
    else:
        print(promptSum(0))

def maxNumber(firstNum, secondNum, thridNum):
    if (firstNum > secondNum and firstNum > thirdNum):
        return firstNum
    elif (secondNum > thirdNum):
        return secondNum
    else:
        return thirdNum


firstNum = int(input("Enter Number: "))
secondNum = int(input("Enter Number: "))
thirdNum = int(input("Enter Number: "))

checkSum(firstNum, secondNum, thirdNum)
print("Max number:", maxNumber(firstNum, secondNum, thirdNum))
