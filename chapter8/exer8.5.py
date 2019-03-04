# Exercise 8.5 
# Exercise 8.5		Write a program to read through the mail box data and when you
#					find line that starts with “From”, you will split the line into words using the split
#					function. We are interested in who sent the message which is the second word on the From line.

fname = input('Enter a file name:')
try:
	fopen = open(fname)
except:
	print('Input right name')
	exit()

lists = None		#this codes means removing the repetitive address
count = 0
for line in fopen:
	if not line.startswith('From'):
		continue
	else:
		words = line.split()
		if lists == None:
			lists = [words[1]]
		if words[1] in lists:
			continue
		else:
			print(words[1])
			lists = lists + [words[1]]
			count = count + 1
print('There were %d in the file with from as the first word' % count)

count1 = 0	# this code distinguish the code above, don't remove repetitive address
fopen1 = open(fname)
for line in fopen1:
	if not line.startswith('From'):
		continue
	else:
		words = line.split()
		print(words[1])
		count1 = count1 + 1
print('There were %d in the file with from as the first word' % count1)
