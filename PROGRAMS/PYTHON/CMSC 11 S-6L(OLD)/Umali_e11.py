'''

Harold S. Umali
April 22, 2016
Description: Recursion of multiplication in terms of addition (eg. 2*5=2+2+2+2+2 or 5*2=5+5)

Plus bonus included

'''

def multiadd(x,y):
	if y==0: 
		## Base case: if multiplier is 0, return 0; used when y is input as 0
		return 0
	elif y==1: 
		## Base case: if multiplier is 1, return self
		return x
	else: 
		## Recursive step: for every recursion, y decrements until it reaches base case y==1
		return x + multiadd(x,y-1) 
		##

def divsub(x,y,month): ## Bonus
	if x==0: 
		return 0
	elif x<y:
		return 1
	elif y==0:
		return 'no'
	else: 
		return 1 + divsub(x-y,y,month) 

def bonus():
	'''
You borrowed Php x from your seatmate. If you promised to pay Php y every month,
how many months do you need to pay your debt completely before your seatmate
kills you? Rawr!
	'''
i=1

while i!=0:
	i=int(input("[1] Exercise [2] BONUS [0] Exit: "))
	if i==1:
		n=int(input("Enter number: ")) 

		add=int(input("Enter number of times added: ")) ## Number of time n adds to itself

		print(multiadd(n,add))

	#############################################################################################
	
	elif i==2:
		input("BONUS! Enter to continue...")
		print(bonus.__doc__,"\n(...wut?)")
		input(" Press enter to continue...")
		month_count=0
		print()
		borrow=int(input("Enter money burrowed: "))
		pay=int(input("Enter payment per month: "))
		
		print("There is/are",divsub(borrow,pay,month_count),"month/s left to pay debt. :3")
		if pay==0:
			input("You are dead... Press enter to quit :P")
			break
		if divsub(borrow,pay,month_count)==1:
			print("You need not pay, mate :3")

	else:
		break

