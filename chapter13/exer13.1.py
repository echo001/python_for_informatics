# Exercise 13.1
# Exercise 13.1			Change the program that retrieves twitter data (twitter2.py) 
#						to also print out the location for each of the friends indented 
#						under the name by two spaces as follows:

import urllib
import xml.etree.ElementTree as ET

twitter_url = 'http://api.twitter.com/l/statuses/friends/ACCT.xml'

while True:
	print ' '
	acct = raw_input('Enter twitter acount : ')
	if (len(acct) < 1) : break
	url = twitter_url.replace('ACCT',acct)
	print 'Retrieving',url
	document = urllib.urlopen(url).read()
	print 'Retrived',len(document),' characters'
	tree = ET.fromstring(document)
	count = 0
	for user in tree.findall('user'):
		count += 1
		if count > 4:break
		print user.find('screen_name').text
		status = user.find('status')
		if status:
			txt = status.find('text').text
			print '  ',txt[:50]
		print user.find('location').text



