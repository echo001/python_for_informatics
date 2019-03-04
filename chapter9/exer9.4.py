# Exercise 9.4 
# Exercise 9.4			Write a program to read through a mail log, and figure out who had
#						the most messages in the file. The program looks for “From” lines and takes the
#						second parameter on those lines as the person who sent the mail.The program creates a Python dictionary 
#						that maps the sender’s address to the total number of messages for that person.
#						After all the data has been read the program looks through the dictionary using
#						a maximum loop (see Section 5.7.2) to find who has the most messages and how many messages the person has.

def read_file_count(filename):
	try:
		fopen = open(filename)
#		print(fopen)
	except:
		return 'invalid'
	personcount = dict()
	for line in fopen:
		words = line.split()
		if not line.startswith('From '):
			continue
		try:	# if words[2] is not existed,maybe causing wrong
			personcount[words[1]] = personcount.get(words[1],0) + 1	#gain the value of dict'key and count
		except:
			continue
	maxinum = maxinum_check(personcount)
	return maxinum

def maxinum_check(personcount):		# to get the most times that email's name appears from dictionary(personcount)
	maxnum = keyrecord = None
	for keysigle in personcount:
		if maxnum == None:
			maxnum = personcount[keysigle]
			keyrecord = keysigle
		elif personcount[keysigle] > maxnum:
			maxnum = personcount[keysigle]
			keyrecord = keysigle
	return keyrecord,maxnum


filename = input('Enter a file name:')
count = read_file_count(filename)
print(count)