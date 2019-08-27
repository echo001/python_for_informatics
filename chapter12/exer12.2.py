# Exercise 12.2
# Exercise 12.2			Change your socket program so that it counts the number of 
#						characters it has received and stops displaying any text after
#						it has shown 3000 characters. The program should retrieve the 
#						entire document and count the total number of characters and 
#						display the count of the number of characters at the end of 
#						the document

import socket
import ast
import sys

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
user_input = raw_input('Enter URL : ')
url = user_input.split('/')	#use split to break the url 

try:
	mysock.connect((url[2],80))	#extract the host name for the socket connect call
	mysock.send('GET ' + user_input + ' HTTP/1.0\n\n')

	flag = 0
	count = dict()
	while True:
		data = mysock.recv(512)
		if( len(data) < 1 ):
			break
		for word in data:
			count[word] = count.get(word,0) + 1	#count characters 
			flag += 1
			if(flag <= 3000):	#stop displaying text after showing 3000 characters
				sys.stdout.write(word)	#output no space and no line feed
	print '\n'
	print count
	mysock.close()

except:
	print 'Error input,please check the url'
