# Exercise 10.3
# Exercise 10.3			Write a function called most_frequent that takes a string and prints the letters 
#						in decreasing order of frequency. Find text samples from several different 
#						languages and see how letter frequency varies between languages. 
#						Compare your results with the tables at wikipedia.org/wiki/Letter_frequencies

import string
def most_frequent(filename)	:
	try:
		fhand = open(filename)
	except:
		return 'Invalid'
	lettercount = dict()
	for line in fhand:
		line = line.translate(string.punctuation)  #translate will cut off all of punctuation
#		print(line)
		line = line.lower()
		words = line.split()
		for word in words:
			for letter in word:
				if letter in string.punctuation:	#cut off all special chars
					letter = letter.replace(letter,"")
					continue
				lettercount[letter] = lettercount.get(letter,0) + 1	#count all letters including number and letters
	#count frequence by creating a list of tuple
	letterlist = list()
	for key,val in lettercount.items():
		letterlist.append((val,key))
	letterlist.sort(reverse=True)
	return letterlist

filename = input('Enter a filename:')
lettercount = most_frequent(filename)
if lettercount is 'Invalid':
	print('Invalid')
else:
	for key,val in lettercount[:]:
		print(val,key)

