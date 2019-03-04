# Exercise 9.5
# Exercise 9.5		This program records the domain name (instead of the address)
#					where the message was sent from instead of who the mail came from (i.e. the
#					whole e-mail address). At the end of the program print out the contents of your dictionary.


def read_file_count(filename):
	try:
		fhand = open(filename)
	except:
		return 'Invalid'
	allcount = dict()
	for line in fhand:
		words = line.split()
		if not line.startswith('From: '):
			continue
		try:		#maybe existed "From:..."  there is no content will cause allcount[] wrong
			emailaddress = words[1].split("@")[-1]	#cut out string from '@'.eg:1@gmail.com will get gmail.com
			allcount[emailaddress] = allcount.get(emailaddress,0) + 1
		except:
			continue
	return allcount

filename = input('Enter a file name:')
count = read_file_count(filename)
print(count) 
	
