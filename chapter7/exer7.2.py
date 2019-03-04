#Exercise 7.2
#Exercise 7.2   Write a program to prompt for a file name, and then read through
#				the file and look for lines of the form:
#				X-DSPAM-Confidence: 0.8475
#				When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
#				the line to extract the floating point number on the line. Count these lines and the
#				compute the total of the spam confidence values from these lines. When you reach
#				the end of the file, print out the average spam confidence.


filename = input('Enter the file name:')
count = sumnum = 0
try:
	fileopen = open(filename)
except:
	print("can't open this file , check file name ,please")
	exit()
for line in fileopen:
	if not line.startswith('X-DSPAM-Confidence:'):
		continue
	sp = line.find(' ')
	num = line[sp:]		#eg:0.8475 in mbox.txt is 6 characters not a float number,so can't use line[sp+1]
	num = num.rstrip()
	num = float(num)
	sumnum = sumnum + num
	count = count + 1
average = sumnum / count
print(average)
