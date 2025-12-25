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

def sort_help(char_item):

    return char_item["num"]

def sort_dict(char_dict):

    d_list = []
    for k, v in char_dict.items():

        d_list.append({"char": k, "num": v})

    d_list.sort(reverse=True, key=sort_help)

    return d_list
