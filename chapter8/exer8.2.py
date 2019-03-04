# Exercise 8.2 & Exercise 8.3
# Exefcise 8.2 		Figure out which line of the above program is still not properly
#					guarded. See if you can construct a text file which causes the program to
#					fail and then modify the program so that the line is properly guarded and
#					test it to make sure it handles your new text file.
# Exercise 8.3		Rewrite the guardian code in the above example without two if statements. 
#					Instead use a compound logical expression using the and 
#					logical operator with a single if statement.

#the example has a problem which if there is no file named when fopen execte, it will cause the 
#program to fail. Modify this code by using try and except

try:
	fopen = open('mbox.txt')
except:
	print('input right name!')
	exit()

count = 0
for line in fopen:
	words = line.split()
	if len(words) != 0 and words[0] == 'From':		#using 'or'  we can use continue to rewrite code
		print(words[2])
		count = count + 1
print(count)