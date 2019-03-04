# Exercise 8.4 
# Exercise 8.4		Write a program to open the file romeo.txt and read it line by line. 
#					For each line,split the line into a list of words using the split function.
#					For each word, check to see if the word is already in a list. 
#					If the word is not in the list, add it to the list.When the program 
#					completes, sort and print the resulting words in alphabetical order.

fname = input('Enter file:')
try:
	fhand = open(fname)
except:
	print('Input right name!')
	exit()
lists = None
for line in fhand:
#	line.strip()
	words = line.split()	#just split every words,content is always the whole line
	for word in words:		
		if lists == None:	#if the writing isn't '[word]',but 'word',it means str,line24 gets wrong
			lists = [word]	#very important,deciding the type of lists,when use'[]',it means 'list'
		elif word in lists:	#distinguish if word is in lists
			continue
		else:
			lists = lists + [word]	# can't use 'append' or '+word' that's append str's alphabet,
print(lists)						# not list,the second appends str also not list