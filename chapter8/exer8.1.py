#Exercise 8.1
#Exercise 8.1	Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
#				Then write a function called middle that takes a list and returns a new list that
#				contains all but the first and last elements.

def chop(t):
	t = t[1:-2]

def middle(t):
	return t[1:-1]


a = ['a','b','c','d']
print(chop(a))

b = ['a','b','c','d']
t = middle(b)
print(b)
print(t)