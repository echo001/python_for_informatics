# Exercise 11.1 
# Exercise 11.1 		Exercise 11.1 Write a simple program to simulate the operation 
#						of the the grep command on UNIX. Ask the user to enter a 
#						regular expression and count the number of lines that matched 
#						the regular expression:
#				$ python grep.py
#				Enter a regular expression: ˆAuthor
#				mbox.txt had 1798 lines that matched ˆAuthor
import re

def accumulate_line(reg_exp):
	try:
		fhand = open('mbox.txt')
	except:
		print('Open file ERROR!\nPlease check the file')
	count = 0
	for line in fhand:
		line = line.rstrip()
		if re.search(reg_exp,line):
			count += 1
	return count

user_input = input('Enter a regular expression:')
count = accumulate_line(user_input)
print('mbox.txt had %d lines that matched %s' % (count,user_input))
