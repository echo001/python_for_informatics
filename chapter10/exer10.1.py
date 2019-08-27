# Exercise 10.1
# Exercise 10.1			Revise a previous program as follows: Read and parse the “From” lines and pull out 
#						the addresses from the line. Count the number of messages from each person 
#						using a dictionary
#						After all the data has been read print the person with the most commits by creating
#						a list of (count, email) tuples from the dictionary and then sorting the list 
#						in reverse order and print out the person who has the most commits.

def read_email_count(filename):
	try:
		fhand = open(filename)
	except:
		return 'Invalid'
	emailcount = dict()
	for line in fhand:
		words = line.split()
		if not line.startswith('From '):
			continue
		try:
			emailcount[words[1]] = emailcount.get(words[1],0) + 1
		except:
			continue
	# count the most times by creating a list of tuples
	emailsort = list()
	for key,val in emailcount.items():			#items return a list of tuple
		emailsort.append((val,key))
	return emailsort


filename = input('Enter a file name:')
emailcommit = read_email_count(filename)
if emailcommit is 'Invalid':
	print(emailcommit)
else:
	emailcommit.sort(reverse=True)
	for key,val in emailcommit[:1]:
		print(val,key)