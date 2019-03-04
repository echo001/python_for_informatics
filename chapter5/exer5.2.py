#repeatedly get input numbers from users and check if the
#number is an interger or float.when receive 'done',
#ends all.and print maximum and minimum from all valid inputs


def check_user_input():
	number = raw_input('Enter a number:')
	if number == 'done':
		return 'done'
	try:
		num = float(number)
	except:
		print('Invalid input')
		return 'invalid'
	return num

minnum = None
maxnum = None
number = None
while number == None or number != 'done':
	number = check_user_input()
	if number == 'invalid':
		continue
	if minnum == None or maxnum == None:
		maxnum = minnum = number
	if number != 'done':
		if minnum > number:
			minnum = number
		elif maxnum < number:
			maxnum = number
print(maxnum,minnum)