# Exercise 9.3 
# Exercise 9.3 			Write a program that categorizes each mail message by which day of
#						the week the commit was done. To do this look for lines which start with “From”,
#						then look for the third word and then keep a running count of each of the days
#						of the week. At the end of the program print out the contents of your dictionary(order does not matter).

def read_file_count(filename):
	try:
		fopen = open(filename)
	except:
		return 'invalid'
	weekcount = dict()
	for line in fopen:
		words = line.split()
		if not line.startswith('From'):
			continue
		try:	# if words[2] is not existed,maybe causing wrong
			weekcount[words[2]] = weekcount.get(words[2],0) + 1	#gain the value of dict'key and count
		except:
			continue
	return weekcount

filename = input('Enter a file name:')
count = read_file_count(filename)
print(count)