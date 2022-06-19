# Program name: Word Count
# Author: Manomaysubban Narasimha
# Python Version 3.8.3
# Goal: to read a text file and count the total number of
# occurances of each word in the file
import re

def count_words():
    book = open("jane-eyre.txt", 'r')
    content = book.read()
    content_list = re.findall(r'\w+', content)
    '''for i in range(len(content_list)):
        content_list[i] = content_list[i].lower()'''
    # create a dictionary that holds the number of occurances of each word
    word_count = {}
    # loop through each word and add it to the dictionary if it already
    # does not exist, and if it does exist, increase it count
    for word in content_list:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1
    for (key, value) in word_count.items():
        print('"' + str(key) + '"' + ': ' + str(value))
    book.close()

    
def main():
    count_words()


if __name__ == "__main__":
    main()
