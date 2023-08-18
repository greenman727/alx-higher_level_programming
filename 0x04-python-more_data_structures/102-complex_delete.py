def complex_delete(a_dictionary, value):
    for key, value in a_dictionary.keys():
        if a_dictionary[key] == value:
            del a_dictionary[key]
