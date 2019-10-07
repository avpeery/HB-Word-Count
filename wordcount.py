# put your code here.
def count_words(filename):
    """Counts word occurences from a given string file  and returns dictionary

        Input : File path

        Output : dictionary of word counts (Returns dictionary)
    """
    opened_file = open(filename)
    word_count_dict = {}

    for line in opened_file:
        line = line.rstrip()
        words = line.split(" ")

        for word in words:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1

    return word_count_dict
    
    

def print_dictionary(given_dictionary):
    """Prints given dictionary by key, value pairs in strings"""

    
    for word, value in given_dictionary.items():
        print(f"{word} {value}")


print_dictionary(count_words("twain.txt"))