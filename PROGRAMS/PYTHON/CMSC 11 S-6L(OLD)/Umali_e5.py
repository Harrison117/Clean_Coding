'''
Harold S. Umali
February 26, 2015
Description: Getting the N number of prime numbers (until 12)
Reference: 
StackOverflow.com [http://stackoverflow.com/questions/1628949/to-find-first-n-prime-numbers-in-python] (Template of N-Prime-Checker)
DaniWeb.com [https://www.daniweb.com/programming/software-development/threads/233730/to-find-first-n-prime-numbers] (Template)
Python3 Documentation [https://docs.python.org/3.0/tutorial/controlflow.html#break-and-continue-stetements-and-else-clauses-on-loops]

'''

N=int(input("Enter number of Primes: "))
P=1
i=1 
o=N/2
#default command would look like: for x in range(0,int(((N*N/2))-(1)))
#N=4 or N=5
n=N-5+i

if N==1:
    print(int(2))
else:
    if N<=3:
        o=2 #N=3; for x in range(0,5)
    if N>=6:
        i=N-1 #N=6; for x in range(0,13))
    if N>=8:
        i=N+n #N=8;n=4; for x in range(0,28)
    if N>=10: 
        i=N*2 #N=10;n=6; for x in range(0,30)
    if N>=11:
        i=N*2+n #N=11;n=7; for x in range(0,31)
    for x in range(0,int(((N*o))-(i))): #Original N-Prime-Checker template: for x in range (1, (N+1))
        '''This type of range is used since it's been determined that N multiplied
        by itself divided by 2 is the last prime number of N numbers minus (depending
        on the value of i) within the range of 0 to int(((N*o))-(i)) until 12. 
        Inputting N > 12 values would get prime numbers within the range of 0 to 
        int(((N*o))-(i))'''
        c=0
        for y in range(1,P+1): 
            #Finds multipliers for the current number P
            a=P%y 
            #Checks P if it is Prime within the range of 1 and P+1
            if a==0: 
                #If there is no remainder, c counts
                c=c+1
        if c==2: 
            #if 2 remainders occur, a prime number is found. Thus, P will be printed
            print(P)
        else: 
            #Otherwise, the a counter will reset.
            a=a-1
        #Get next number for prime checking
        P=P+1