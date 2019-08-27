# Exercise 12.4 
# Exercise 12.4 		Change the urllinks.py program to extract and count 
#						paragraph(p) tags from the retrieved HTML document and display 
#						the count of the paragraphs as the output of your program. 
#						Do not display the paragraph text - only count them. Test 
#						your program on several small web pages as well as some 
#						larger web pages

import urllib
import re

user_input = raw_input('Enter URL : ')
fhand = urllib.urlopen(user_input)
html = fhand.read()
count = 0
p_tag = re.findall('</p>',html)
for p in p_tag:
	count += 1
print count

