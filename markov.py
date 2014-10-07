#!/usr/bin/env python

import sys
corpus = open("Meteorology.txt")
corpus_dict = {}
word_list =[]

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    for line in corpus:
        words = line.strip().split()
        for i in range(len(words) -1):
            word_list.append((words[i], words[i +1]))
    # print word_list        

    for bigram_tuple in range(len(word_list) -1): 
        corpus_dict[(word_list[bigram_tuple])] = [word_list[bigram_tuple + 1][1]] 
    print corpus_dict

    #for bigram_tuple in range(len(word_list)):
        # print word_list[bigram_tuple]
        #take tuple
        #put as key in dict with empty list as value
        
        #corpus_dict.setdefault([word_list[bigram_tuple]], [])


        #.append([word_list[bigram_tuple] + 1][1])
    #print corpus_dict             

#     return {}

# def make_text(chains):
#     """Takes a dictionary of markov chains and returns random text
#     based off an original text."""
#     return "Here's some random text."

def main():
#     args = sys.argv

#     # Change this to read input_text from a file
#     input_text = "Some text"

      chain_dict = make_chains(corpus)
#     random_text = make_text(chain_dict)
#     print random_text

if __name__ == "__main__":
     main()