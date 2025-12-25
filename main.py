from stats import get_num_words, get_num_chars

def get_book_text(filepath):

    with open(filepath) as fp:
        return fp.read()

def main():

    content = get_book_text("./books/frankenstein.txt")
    words = get_num_words(content)
    print(get_num_chars(content))
    

main()
