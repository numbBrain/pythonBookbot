from stats import get_num_words, get_num_chars, sort_dict

def get_book_text(filepath):

    with open(filepath) as fp:
        return fp.read()

def main():

    content = get_book_text("./books/frankenstein.txt")
    num_of_words = get_num_words(content)
    print(f"Found {num_of_words} total words")
    char_dict = get_num_chars(content)
    sorted_chars = sort_dict(char_dict)

    for elem in sorted_chars:

        if elem["char"].isalpha():

            print(f"{elem["char"]}: {elem["num"]}")

    
    

main()
