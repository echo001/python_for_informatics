#sum counts that the one character appears in a string
#using function to encapsulate 

def count(words,letter):
	count = 0
	for character in words:
		if character == letter:
			count = count + 1
	return count

words = 'banana'
counter = count(words,'b')
print(counter)
