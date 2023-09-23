# run this to check if a word can be printed using the letter combinations provided in the dictionary
# if -q is passed as an argument, the program will ask for a word and print the result
# otherwise, it will print all the words in the provided dataset, that can be printed using the provided dictionary

import sys

# checks if <word> can be printed using elements of <print_with> with a maximum length of <max_length>
# returns a tuple (bool, list) where bool is True if the word can be printed and list is the list of elements used
def printable(word, print_with, max_length=float('inf')):
    if len(word) == 0:
        return (True, [])
    for i in range(min(len(word), max_length)):
        substring = word[:(i+1)]
        if substring in print_with:
            remainder = word[(i+1):]
            if printable(remainder, print_with, max_length)[0]:
                return (True, [substring] + printable(remainder, print_with, max_length)[1])
    return (False, [])

def prettify_breakdown(breakdown, separator=""):
    capitalized = ""
    for elem in breakdown:
        capitalized += elem.title()
        capitalized += separator
    if len(separator) > 0:
        return capitalized[:-len(separator)]
    return capitalized


dataset_path = "./datasets/" # path to the folder containing the datasets

dict_path = dataset_path + "chemical-elements.txt" 

dict_elements = []
with open(dict_path, 'r') as file:
    for line in file:
        dict_elements.append(line.strip().lower())

dict_elements.sort()

words_path = dataset_path + "derewo/parsed/derewo-320000g.txt"

words = []
with open(words_path, 'r') as file:
    for line in file:
        if len(line.strip()) > 0:
            words.append(line.strip().lower())

if "-q" in sys.argv:
    user_input = input("Enter a word: ").lower()
    result = printable(user_input, dict_elements)
    if result[0]:
        print(prettify_breakdown(result[1], " "))
    else:
        print("Cannot be printed")
    exit()

printable_words = []
for word in words:
    result = printable(word, dict_elements)
    if result[0]:
        printable_words.append(word + " => " + prettify_breakdown(result[1]))

print(printable_words)
print("total amount: " + len(printable_words))