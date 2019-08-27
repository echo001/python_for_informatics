# Exercise 11.2
# Exercise 11.2 		Write a program to look for lines of the form 
#						New Revision: 39772
#						And extract the number from each of the lines using a regular 
#						expression and the findall() method. Compute the average of the 
#						umbers and print out the average.

import re
import string

def average_number(filename):
	try:
		fhand = open(filename)
	except:
		print('Can not find file,please check')
	sum_num = count = 0
	for line in fhand:
		line = line.rstrip()
		x = re.findall('^New Revision: ([0-9.]+)',line)		#extract numbers,get a list
		if len(x) > 0 :
			int_x_list = list(map(int,x))	#change string list to int list 
			count += 1
			for int_x in int_x_list:		#do sum for int list
				sum_num += int_x
	aver_num = sum_num / count
	return aver_num

user_input = input('Enter file:')
aver_number = average_number(user_input)
print('%.7f' % aver_number)