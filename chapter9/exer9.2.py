# Exercise 9.2 
# Exercise 9.2 			Dictionaries have a method called get that takes a key and a default
#						value. If the key appears in the dictionary, get returns the corresponding value;
#						otherwise it returns the default value. Use get to write histogram more concisely. 
#						You should be able to eliminate the if statement.

def histogram(s):
	countdic = dict()
	for c in s:
		countdic[c] = countdic.get(c,0) + 1		#get(c,0) will return the value of dict.key,if c isn't existed,it will return 0
	return countdic								#gain the key's value and then dict[] = means assignment

user_input = input('Enter a string:')
counter = histogram(user_input)
print(counter)