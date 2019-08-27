# Exercise 10.2
# Exercise 10.2			This program counts the distribution of the hour of the day for each of the messages.
# 						You can pull the hour from the “From” line by finding the time string and 
#						then splitting that string into parts using the colon character. Once you have 
#						accumulated the counts for each hour, print out the counts, one per line,
#						sorted by hour as shown below	

def time_of_day(filename):
	try:
		fhand = open(filename)
	except:
		return 'Invalid'
	timecount = dict()
	for line in fhand:
		words = line.split()
		if not line.startswith('From '):
			continue
		try:
			timenum = words[5].split(':')[0]
			timecount[timenum] = timecount.get(timenum,0) + 1
		except:
			continue
	#count time by creating a list of tuple
	timelist = list()
	for key,val in timecount.items():
		timelist.append((key,val))
	return timelist

filename = input('Enter a file name:')
timelist = time_of_day(filename)
if timelist is 'Invalid':
	print('Invalid')
else:
	timelist.sort(reverse=False)
	for key,val in timelist[:]:
		print(key,val)