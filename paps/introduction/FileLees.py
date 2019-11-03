file = open('FileLees.txt')

for line in file:
	counterOfChars = 0 
	for char in line.strip(): 
		# print (char)
		counterOfChars += 1 
	print ("er zijn", counterOfChars, "chars in de regel <<<", line.strip(), ">>>")
