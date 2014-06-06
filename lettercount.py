def generate_alphabet():
	output=[]
	alphabet=range(ord('a'),ord('z')+1)
	for item in alphabet:
		output.append(chr(item))
	return output

def read_text(text_file):
	f = open(text_file)
	filetext = f.read()
	file_text_lowercase=filetext.lower()
	char_list=list(file_text_lowercase)
	return char_list

def count_letters(char_list):
	letter_tallies=[]
	alphabet=generate_alphabet()
	for letter in alphabet:
		total=char_list.count(letter)
		letter_tallies.append(total)
	return letter_tallies

def print_letters(letter_tallies):
	for tally in letter_tallies:
		print tally

		 
def main():
	char_list=read_text("twain.txt")

	letter_tallies=count_letters(char_list)

	print_letters(letter_tallies)




if __name__ == '__main__':
	main()