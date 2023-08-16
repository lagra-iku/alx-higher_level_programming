#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_a_dictionary = sorted(a_dictionary)
    for key in sorted_a_dictionary:
        print("{}: {}".format(key, a_dictionary[key]))
