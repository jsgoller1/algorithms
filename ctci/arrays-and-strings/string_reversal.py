
def correct_reversal(string):
	if type(string) is not str:
		return False
	return string[::-1]

def unnecessary_reversal(string):
	new_string = ''
	for each in range(len(string)-1, -1, -1):
		new_string += string[each]
	return new_string

if __name__ == '__main__':
	string = "This is the string forwards."
	print string
	print api_reversal(string)
	print unnecessary_reversal(string)
