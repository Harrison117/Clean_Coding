'''

@author Harold Umali
Originally created: March 11, 2016
Revised in: August 27 2017
Description: Calculator program; has basic arithmetic operations and other forms
    of operations which are modulo, exponentiation and factorial operations

    UPDATED(08/27):
        - implemented alternate string formatting =3
        - made use of static global and english-friendly variables for readability
        - recursion functionality added
        - program almost has no number values shown =3

        80 less readable lines (OLD) VS 124 more readable lines (new)

'''

NULL = 0
FIRST = 1
SECOND = 2

ADD = 1
SUBTRACT = 2
MULTIPLY = 3
DIVIDE = 4
MODULO = 5
EXPONENT = 6
FACTORIAL = 7

def promptMessage(typeOfMessage, operands):
    if typeOfMessage == ADD:
        print("Enter {} number to add: ".format("1st" if operands == FIRST else "2nd"), end="")
    elif typeOfMessage == SUBTRACT:
        print("Enter {} number to Subtract: ".format("1st" if operands == FIRST else "2nd"), end="")
    elif typeOfMessage == MULTIPLY:
        print("Enter {} number to multiply: ".format("1st" if operands == FIRST else "2nd"), end="")
    elif typeOfMessage == DIVIDE or typeOfMessage == MODULO:
        print("{}".format("Enter number to be divided: " if operands == FIRST else "Divide number by: "), end="")
    elif typeOfMessage == EXPONENT:
        print("Enter {}: ".format("base number" if operands == FIRST else "exponent"), end="")
    elif typeOfMessage == FACTORIAL:
        print("Enter number to factorialize: ", end="")
    else:
        print("Exiting...")
    return

def additionOperation(adden1,adden2):
    return adden1+adden2

def subtractionOperation(minuend,subtrahend):
    return minuend-subtrahend

def multiplicationOperation(factor1,factor2):
    return factor1*factor2

def divisionOperation(dividend,divisor):
    return dividend/divisor

def moduloOperation(dividend,divisor):
    return dividend%divisor

def exponentiationOperation(base,exponent):
    if exponent == 1:
        return base
    else:
        return base*exponentiationOperation(base,exponent-1)

def factorialOperation(factor):
    if factor == 2:
        return factor
    else:
        return factor*factorialOperation(factor-1)

stateOfProgram = True
inputChoice = NULL
operand1 = NULL
operand2 = NULL

while stateOfProgram == True:
    print("Menu:")
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[5] Modulo")
    print("[6] Exponentiation")
    print("[7] Factorial")
    print("[8] Exit")

    inputChoice = int(input("Enter Choice: "))
    if inputChoice == ADD:
        promptMessage(ADD,FIRST)
        operand1 = int(input())

        promptMessage(ADD,SECOND)
        operand2 = int(input())
        print("Sum:",additionOperation(operand1,operand2))

    elif inputChoice == SUBTRACT:
        promptMessage(SUBTRACT,FIRST)
        operand1 = int(input())

        promptMessage(SUBTRACT,SECOND)
        operand2 = int(input())
        print("Difference:",subtractionOperation(operand1,operand2))

    elif inputChoice == MULTIPLY:
        promptMessage(MULTIPLY,FIRST)
        operand1 = int(input())

        promptMessage(MULTIPLY,SECOND)
        operand2 = int(input())
        print("Product:",multiplicationOperation(operand1,operand2))

    elif inputChoice == DIVIDE:
        promptMessage(DIVIDE,FIRST)
        operand1 = int(input())

        promptMessage(DIVIDE,SECOND)
        operand2 = int(input())
        print("Quotient:",divisionOperation(operand1,operand2))

    elif inputChoice == MODULO:
        promptMessage(MODULO,FIRST)
        operand1 = int(input())

        promptMessage(MODULO,SECOND)
        operand2 = int(input())
        print("Remainder:",moduloOperation(operand1,operand2))

    elif inputChoice == EXPONENT:
        promptMessage(EXPONENT,FIRST)
        operand1 = int(input())

        promptMessage(EXPONENT,SECOND)
        operand2 = int(input())
        print("Value:",exponentiationOperation(operand1,operand2))

    elif inputChoice == FACTORIAL:
        promptMessage(MULTIPLY,FIRST)
        operand1 = int(input())
        print("Product:",factorialOperation(operand1))

    else:
        stateOfProgram = False
"""
def menu():
    '''Menu:
    [1] Addition
    [2] Subtraction
    [3] Multiplication
    [4] Division
    [5] Modulo
    [6] Exponentiation
    [7] Factorial
    [8] Exit'''
def add(a,b): #addition
    x=a+b
    return x
def minus(a,b): #subtraction
    x=a-b
    return x
def multiply(a,b): #multiplication
    x=a*b
    return x
def divide(a,b): #division
    x=a/b
    return x
def mod(a,b): #modulo
    x=a%b
    return x
def exp(a,b): #exponential
    x=a**b
    return x
def fac(a): #factorial
    m=a-1
    x=a
    while m!=1:
        x=x*m
        m=m-1
    return x

def operations(choice):
    if choice==1:
        a=int(input("Enter First number: "))
        b=int(input("Enter Second number: "))
        print(add(a,b)) #calls the fuction and applies the input actual parameters
    elif choice==2:
        a=int(input("Enter First number: "))
        b=int(input("Enter Second number: "))
        print(minus(a,b)) #same as the previous choice
    elif choice==3:
        a=int(input("Enter Factor: "))
        b=int(input("Enter Factor: "))
        print(multiply(a,b))
    elif choice==4:
        a=int(input("Enter Dividen: "))
        b=int(input("Enter Divisor: "))
        print(divide(a,b))
    elif choice==5:
        a=int(input("Enter First number: "))
        b=int(input("Enter Second number: "))
        print(mod(a,b))
    elif choice==6:
        a=int(input("Enter number: "))
        b=int(input("Enter Exponent: "))
        print(exp(a,b))
    elif choice==7:
        a=int(input("Enter number: "))
        print(fac(a))
def cont(): #Continuity of program
    if n==8:
        return False
    return True
P=True
while P: #Program runs while True
    print(menu.__doc__) #Prints the menu
    n=int(input("Enter Operation: "))
    operations(n) #enters the n in operations(n) function
    c=cont()
    if c:  #if the choice is not 8, function will return true
        for i in range(0,5):
            print()
        continue
    else:  #if the choice is 8, function will return false
        input("See you again!!! Press Enter again to exit...")
        break
"""
