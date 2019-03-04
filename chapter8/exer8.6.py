# Exercise 8.6 
# Exercise 8.6			Rewrite the program that prompts the user for a list of numbers and
#						prints out the maximum and minimum of the numbers at the end when the user
#						enters “done”. Write the program to store the numbers the user enters in a list and use the max() 
#						and min() fuctions to compute the maximum and minimum numbers after the loop completes.

def check_user_input():
	number = input('Enter a number:')
	if number == 'done':
		return 'done'
	try:
		num = float(number)
	except:
		return 'Invalid'
	return num

number = None
numlist = None
while number == None or number != 'done':
	number = check_user_input()
	if number == 'Invalid' or number == 'done':
		continue
	if numlist == None:
		numlist = [number]
	numlist = numlist + [number]
try:
	maxnum = max(numlist)
	minnum = min(numlist)
	print('Maxinum:%.1f\nMininum:%.1f' % (float(maxnum),float(minnum)))
except:
	exit()