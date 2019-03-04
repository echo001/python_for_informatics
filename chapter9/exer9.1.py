# Exercise 9.1 
# Exercise 9.1			Write a function that reads the words in words.txt and stores them
#						as keys in a dictionary. It doesn’t matter what the values are. Then you can use
#						the in operator as a fast way to check whether a string is in the dictionary.

def read_store_dict():
	try:
		fopen = open('words.txt')
	except:
		print('no files named "words.txt"')
		exit()
	worddict = dict()
	for line in fopen:	#read the content of words.txt and read line by line
		words = line.split()
		for word in words:		#give dict the key
			worddict[word] = None
	return worddict

dictkey = input('Enter a key:')
worddict = read_store_dict()
#print(worddict)
if dictkey in worddict:		#check the input from user if is stored in dict.keys
	print('True')
else:
	print('False')

