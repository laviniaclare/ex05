def read_text():
    f = open("myfile.txt")
    filetext = f.read()
    char_list=list(filetext)
    char_list_lower=char_list.lower
    return char_list_lower

def count_letters(char_list_lower):
	letter_tallies=[]
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in alphabet:
        total=char_list_lower.count(letter)
        letter_tallies.append(total)

def print_letters():
	

         
def main():


if __name__ == '__main__':
	main()