#!/usr/bin/env python

import sys
import random


def make_chains():
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    corpus = open("Meteorology.txt")
    corpus_dict = {}
    read_file = corpus.read()
    split_file = read_file.split()
    for i in range(len(split_file) -2):
        if (split_file[i], split_file[i + 1]) in corpus_dict: 
            value = corpus_dict[(split_file[i], split_file[i+1])] # = [words[i+1]]
            value.append(split_file[i +2])
            corpus_dict[(split_file[i], split_file[i + 1])] = value


        else: 
            #make new key, value entry in dict
            corpus_dict[(split_file[i], split_file[i +1])] = [split_file[i+2]]
    return corpus_dict


def make_text(chains):
# #     """Takes a dictionary of markov chains and returns random text
# #     based off an original text."""
# #     #return "Here's some random text."
# #     #generate a random starting point
    key_list =[]
        #creates a list of keys so that we can manipulate the index
    for k in chains.keys():
        key_list.append(k)
    # print key_list

    starting_point = random.choice(key_list)
    count = 0 
    while count < 10:
        key = starting_point
        # print "key", key
        chain_one = random.choice(chains[key])
        # print "value", chain_one
        #find this tuple
        if chains[(key[1], chain_one)] in chains:
            #new_chain returns a random value from this tuple
            new_chain = random.choice(chains[(key[1], chain_one)])
            print new_chain
        count += 1


def main():
#     args = sys.argv

#   Change this to read input_text from a file
#   input_text = "Some text"

    chain_dict = make_chains()
    random_text = make_text(chain_dict)
#   print random_text

if __name__ == "__main__":
     main()