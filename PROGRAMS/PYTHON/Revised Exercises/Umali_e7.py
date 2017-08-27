'''

@author Harold Umali

Originally Created in: March 18 2015
Revised in: August 27 2017
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

    UPDATED (08/27):
        - separated some string manipulation methods into functions
        - again, improve readability

'''
CAPITAL_TO_SMALL_LETTER_INCREMENT = 32
ASCII_TO_INTEGER_DECREMENT = 48

## ascii values of integers ranges from 48 to 57
NUMBER_0 = 48
NUMBER_9 = 57

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
        elif ord(character) >= SMALL_a and ord(character) <= SMALL_z or ord(character) >= NUMBER_0 and ord(character) <= NUMBER_9:

            ## add the current character to char
            temporaryStringHolder += character

        # ignores all the special characters having ascii values not within the given ranges above
        else:
            continue

    return temporaryStringHolder

def splitWord(wordGiven, middleIndex, endIndex):
    firstHalfWord = ""
    secondHalfWord = ""

    if len(wordGiven) % 2 == EVEN_LENGTH:
        ## means get word from the first to the middle letters
        firstHalfWord = wordGiven[START_INDEX:middleIndex]
    else:
        ## means get word from the first to the middle letters
        ##  Note: it wont include the middle character because it is equal to itself
        firstHalfWord = wordGiven[START_INDEX:middleIndex+1]

    ## means get word from the middle to the last letters
    secondHalfWord = wordGiven[middleIndex:endIndex]

    return firstHalfWord, secondHalfWord

def reverseOf(wordGiven):
    ## returns 'string[begin:end:step]' format
    return wordGiven[::-1]

print("Enter numbers/words/phrases/sentences (separate in commas): ")
wordInputs = input()

## assigns the given inputs separated from commas into the list
stringList = wordInputs.split(',')

for stringMember in stringList:
    ## new word will contain purely small letters only
    newWord = removeSpecialCase(stringMember)

    wordSize = len(newWord) ## also the end index of the word
    midIndex = int(wordSize/2)

    firstHalfNewWord, secondHalfNewWord = splitWord(newWord, midIndex, wordSize)

    if firstHalfNewWord == reverseOf(secondHalfNewWord):
        print("{} is a palindrome.".format(stringMember))
    else:
        print("{} is not a palindrome.".format(stringMember))
