# put your code here.
def count_words(filename):
    opened_file = open(filename)
    word_count_dict = {}
    
    for line in opened_file:
        line = line.rstrip()
        words = line.split(" ")

        for word in words:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1
    
    return word_count_dict

print(count_words("test.txt"))
