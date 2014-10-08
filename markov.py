#!/usr/bin/env python

import sys
import random
corpus = open("Meteorology.txt")
corpus_dict = {}
word_list =[]

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    for line in corpus:
        words = line.strip().split()
        for i in range(len(words) -2):
            if words[i] in corpus_dict: 
                print corpus_dict[words[i]]
                #append value to dict 
                # corpus_dict[words[i]]         .append(words[i+1]) 
                # corpus_dict.setdefault(words[i], []).append(words[i+1])
            else: 
                #make new key entry in dict
                #append value to dict  
                # corpus_dict[(words[i], words[i +1])] = words[i+2]   
                pass
            #((words[i], words[i +2]))
    # print word_list        

    # for bigram_tuple in range(len(word_list) -1): 
    #     corpus_dict[(word_list[bigram_tuple])] = [word_list[bigram_tuple + 1][1]] 
    print corpus_dict  

# def make_text(chains):
#     """Takes a dictionary of markov chains and returns random text
#     based off an original text."""
#     #return "Here's some random text."
#     #generate a random starting point
#     while True: 
#         #read through the list of keys
#         if  

#         for num in range(1, 10): 
#             my_list =[]
#             #creates a list of keys so that we can manipulate the index
#             for k in corpus_dict.keys():
#                 my_list.append(k)

#             random_integer = 
            
#             print my_list[random.randint[num]]
    # for k in range(len(corpus_dict) -1):

        #can't use random.seed because it's output is a number
        #print random.seed([corpus_dict[k]])

    #save our output to a list or something....

def main():
#     args = sys.argv

#   Change this to read input_text from a file
#   input_text = "Some text"

    chain_dict = make_chains(corpus)
#    random_text = make_text(chain_dict)
#   print random_text

if __name__ == "__main__":
     main()