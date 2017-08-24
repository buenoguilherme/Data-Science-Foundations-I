try:
	f = open('words323.txt', 'r')
except IOError as err:
	print('Error reading file: ' + str(err))