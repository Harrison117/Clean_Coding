'''

Harold S. Umali
Febuary 19. 2016
Description: If-else statement - Given three inputs, checking and telling if
  there is any pair that would equal to the third number and if the highest
  number among the three is even or odd.

'''

x,y,z=int(input("Enter number: ")),int(input("Enter number: ")),int(input("Enter number: "))

#Checks the numbers if there are  any pairs resulting the third number
if x+y==z: #prints first line. if not true then proceed to second condition
    print(x,"plus",y,"is equal to",z)
elif y+z==x: #if not true then proceed to third condition
    print(y,"plus",z,"is equal to",x)
elif z+x==y:#if not true then proceed to last condition
    print(y,"plus",z,"is equal to",x)
else: #if none of the above statements are true, this will print
    print("No pair is equal to the other number.")

#Checks for the highest numbers and if that number is odd or even
if x>y and x>z:
    if x%2==0:
        #if it has no remainder, even
        print(x,", the highest number is even.")
    else:
        #else, odd
        print(x,", the highest number is odd.")
elif y>z:
    if y%2==0:
        print(y,", the highest number is even.")
    else:
        print(y,", the highest number is odd.")
else:
    if z%2==0:
        print(z,", the highest number is even.")
    else:
        print(z,", the highest number is odd.")
