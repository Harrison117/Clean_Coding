'''
@author Harold S. Umali
Originally Created in: February 26, 2015
Revised in: August 26 2017
Description: Given an input N from user, get the N number of prime numbers
    (not to be confused with getting prime numbers from 2 up to N)

    UPDATED(08/26):
        - revised the cringy hard-coded crap >.<
        - changed variable names for readability and self-documenting
            improvement
        - improved logic of the program
        - no point in comparing lines made (old code is crap...)

'''
EVEN = 0
BASE_CASE = 2
MAX_FACTOR_OF_PRIME = 2


factors = 1     ## initially one (1 as a factor)
counter = 0     ## counts up to N prime numbers
numberToBeTested = BASE_CASE    ## starts at prime number 2
inputNumber = int(input("Enter a number: "))

print("The prime numbers are: ")

while(counter < inputNumber):
    if inputNumber == EVEN:
        print("none...")
        break
    else:
        if inputNumber == 1:
            print(BASE_CASE)
            break
        for i in range(BASE_CASE, numberToBeTested+1):
            if numberToBeTested % i == 0:
                factors += 1

    if factors <= MAX_FACTOR_OF_PRIME:
        print(numberToBeTested)
        counter += 1

    numberToBeTested += 1   ## increment
    factors = 1             ## reset value of prime factors
