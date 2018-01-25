"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    output = []
    if len(list1) == 0:
        return output
    output.append(list1[0])
    for item in list1:
        if item != output[-1]:
            output.append(item)
    return output

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    output = []
    idx1 = 0
    idx2 = 0
    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] == list2[idx2]:
            output.append(list1[idx1])
            idx1 += 1
            idx2 += 1
        elif list1[idx1] < list2[idx2]:
            #output.append(list1[idx1])
            idx1 += 1
        else:
            #output.append(list2[idx2])
            idx2 += 1
        #print(idx1)
        #print(idx2)
        #print("---")
    #if idx1 < len(list1):
    #    for idx in range(idx1, len(list1)):
    #        output.append(list1[idx])
    #if idx2 < len(list2):
    #    for idx in range(idx2, len(list2)):
    #        output.append(list2[idx])
    return output

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """   
    output = []
    temp_list1 = list(list1)
    temp_list2 = list(list2)
    while temp_list1 and temp_list2:
        if temp_list1 < temp_list2:
            output.append(temp_list1.pop(0))
        else:
            output.append(temp_list2.pop(0))
    return output + temp_list1 + temp_list2
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) < 2:
        return list1
    else:
        mid_point = len(list1) / 2
        temp_list1 = list(list1[:mid_point])
        temp_list2 = list(list1[mid_point:])
        return merge(merge_sort(temp_list1), merge_sort(temp_list2))

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return ['']
    else:
        first = word[0]
        rest = word[1:]
        rest_strings = gen_all_strings(rest)
        new_strings = []
        for item in rest_strings:
            for pos in range(len(item)+1):
                new_strings.append(item[:pos] + first + item[pos:])
        return rest_strings + new_strings

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)
    data = netfile.readlines()
    words_dict = [line[:-1] for line in data]
    return words_dict

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()