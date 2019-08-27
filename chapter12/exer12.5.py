# Exercise 12.5
# Exercise 12.5			(Advanced) Change the socket program so that it only shows 
#						data after the headers and a blank line have been received. 
#						Remember that recv is receiving characters (newlines and all)
#						- not lines.

import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
user_input = raw_input('Enter URL : ')
url = user_input.split('/')

try:
	mysock.connect((url[2],80))
	mysock.send('GET ' + user_input + ' HTTP/1.0\n\n')
	content = ''
	while True:
		data = mysock.recv(512)
		if( len(data) < 1 ):
			break
		content += data
	output_point = content.find('\r\n\r\n')
	print(content[output_point+4:])
	mysock.close()
except:
	print 'Error input,please check the url'