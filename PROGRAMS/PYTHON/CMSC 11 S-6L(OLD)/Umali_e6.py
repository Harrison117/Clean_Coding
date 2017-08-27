'''

Harold Umali
March 11, 2016
Description: Propmts the user an operation and enters numbers 
  according to the user's selected operation.

'''
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