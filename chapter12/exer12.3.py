# Exercise 12.3
# Exercise 12.3			Use urllib to replicate the previous exercise of (1) 
#						retrieving the document from a URL, (2) displaying up to 
#						3000 characters, and (3) counting the overall number of 
#						characters in the document. Don not worry about the headers 
#						for this exercise, simply show the first 3000 characters of 
#						the document contents.

import urllib
import sys

user_input = raw_input('Enter URL : ')
try:
	fhand = urllib.urlopen(user_input)
	count = dict()
	flag = 0
	for line in fhand:
		for word in line:
			count[word] = count.get(word,0) + 1	#count characters 
			flag += 1
			if ( flag <= 3000):		#stop displaying text after showing 3000 characters
				sys.stdout.write(word)	#output no space and no line feed
	print('\n')
	print(count)
except:
	print('Error input,please check the url')
