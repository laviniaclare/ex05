def put_text_into_list():
    f = open("myfile.txt")
    filetext = f.read()
    char_list=list(filetext)
    char_list_lower=char_list.lower
    return char_list_lower

def parse_text(char_list_lower):
    a = 0
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in alphabet:
        char_list_lower.count(letter)
         
def main():