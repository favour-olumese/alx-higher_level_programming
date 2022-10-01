#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    reverse_dict = sorted(a_dictionary.items(), reverse=True)
    # reverse_dict[0] is the tuple of the key and the value
    # having the highest value.
    # reverse_dict[0][0] is the key.
    return reverse_dict[0][0]
