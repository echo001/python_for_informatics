#repeatedly read numbers from user's input,when input string
#print 'invalid input' ,and then continue next input.
#when input 'done',ends up input.finnally get all valid input
#compute sum , loop count ,and average

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

numsum = 0
count = 0
number = None
while number == None or number != 'done':
	number = check_user_input()
	if number == 'invalid':
		continue
	if number != 'done':
		count = count + 1
		numsum = numsum + number
average = numsum / count
print(numsum,count,average)