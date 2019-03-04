#Exercise 7.1

#Exercise 7.1    Write a program to read through a file and print the contents of the
#			     file (line by line) all in upper case. 


filename = input('Enter a file name:')

try:
	fileopen = open(filename)
except:
	print("Can't open this file,check file name,please")
	exit()

for line in fileopen:
	line = line.rstrip()
	line = line.upper()
	print(line)
