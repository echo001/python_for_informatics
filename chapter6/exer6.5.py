#Exercise 6.5


# Exercise 6.5  str = 'X-DSPAM-Confidence: 0.8475'
#				Use find and string slicing to extract the portion of the string after the colon
#				character and then use the float function to convert the extracted string into a
#				floating point number.

strings = 'X-DSPAM-Confidence: 0.8475'
firstpo = strings.find(' ')
number = strings[firstpo:]
flonum = float(number)
print(flonum)