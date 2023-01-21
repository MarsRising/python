

def linear_search_dictionary(dictionary, target):
    if target in dictionary.values():
        x = list(dictionary.keys())[list(dictionary.values()).index(target)]
        print("Found at key", x)
        return x
    else:        
        print ("Target is not in the list")
        return -1

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)