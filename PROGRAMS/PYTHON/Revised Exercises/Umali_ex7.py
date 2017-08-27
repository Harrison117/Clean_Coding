'''

Harold S. Umali
March 18. 2016
Description: In n strings which is given by the user, checks whether string a, also
  given by the user, is a palindrome or not. Works in numeral, word, phrase or sentence
  level

  PROCEDURE:
    - ask for word/s
    - get word/s
    - remove special cases:
        - special characters
        - spaces
        - capital letters
    - split word
    - reverse the last half
    - compare
    - repeat

'''
CAPITAL_TO_SMALL_LETTER_INCREMENT = 32

## ascii values of capital letters ranges from 65 to 90
CAPITAL_A = 65
CAPITAL_Z = 90

## ascii values of small letters range from 97 to 122
SMALL_a = 97
SMALL_z = 122

START_INDEX = 0
EVEN_LENGTH = 0

def removeSpecialCase(wordGiven):

    temporaryStringHolder = ""

    for character in wordGiven:
        ## checks ascii value of the character if it is a caputal letter
        ##     * function ord(<value>) converts the char into integer
        if ord(character) >= CAPITAL_A and ord(character) <= CAPITAL_Z:

            ## convert the character into small letters
            temporaryStringHolder += chr(ord(character) + CAPITAL_TO_SMALL_LETTER_INCREMENT)
            continue

        ## checks ascii value of the character if it is a small letter
        elif ord(character) >= SMALL_a and ord(character) <= SMALL_z:

            ## add the current character to char
            temporaryStringHolder += character

        # ignores all the special characters having ascii values not within the given ranges above
        else:
            continue

    return temporaryStringHolder

def splitWord(wordGiven):
    firstHalfWord = ""
    secondHalfWord = ""

    if len(word) % 2 == EVEN_LENGTH:
        ## means get word from the first to the middle letters
        firstHalfWord = word[START_INDEX:middleIndex]
    else:
        ## means get word from the first to the middle letters
        firstHalfWord = word[START_INDEX:middleIndex+1]

    ## means get word from the middle to the last letters
    secondHalfWord = word[middleIndex:endIndex]

    return

word = input("Enter word/phrase: ")
endIndex = len(word) ## also the size of the word
middleIndex = int(endIndex/2)

print(firstHalfWord,secondHalfWord)

for letter in word:
    pass

"""
def isPalindrome():
    i=0
    if z==y[-(i)]: #checks the current letter and y[-i] letter if equal
        i=i+1 #index update
        return True
    return False

l=[]
b="" #stores a word
n=int(input("Enter number of strings: "))
for x in range(0,n):
    a=input("Enter string: ")
    b=str.lower(a) #stores a to b to be lower-cased
    l.append(b)
    #check list
    #print(l)
#########################################################################################

for y in l: #y gets elements in l
    for z in y: #z gets the characters of element y
        if z=="," or z=="." or z==" ":
            continue
            #skips the special characters
        p=isPalindrome() #initiate isPalindrome function
    if p:
        print(y,"is a palindrome")
    else:
        print(y,"is not a palindrome")
"""
