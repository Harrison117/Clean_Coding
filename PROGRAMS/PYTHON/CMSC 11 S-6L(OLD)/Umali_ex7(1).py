'''

Harold S. Umali
March 18. 2016
Description: In n strings which is given by the user, checks whether string a, also
  given by the user, is a palindrome or not. Works in numeral, word, phrase or sentence
  level
  
'''
def isPalindrome():
    i=0
    if z==y[-(i)]: #checks the current letter and -i letter if equal
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
    print(l)
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
       
