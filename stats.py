def get_num_words(str):

    return len(str.split())

def get_num_chars(str):

    str = str.lower()
    char_dict = dict()

    for c in str:

        if c in char_dict:
            char_dict[c] += 1

        else:
            char_dict[c] = 1


    return char_dict
