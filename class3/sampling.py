import sys
import random
from dictogram import *

            

def stochastic_sampling(weighted_hist):
    """Randomly choose a word in weighted histogram based on cumulative weights"""
    rand_percent = random.uniform(0,1)
    cum_weight = 0
    for token in weighted_hist:
        cum_weight += word[1]
        if cum_weight > rand_percent:
            return word[0]

def weighted_dict(dictogram):
    """Convert dictogram into weighted histogram"""
    total = sum([dictogram.values()])
    weight_dict = {}
    for key,val in dictogram.items()
        weight_dict[key] = val/total
    print(weight_dict)
    return weight_dict

def weighted_list(listogram):
    """Return a weighted listogram from list"""
    weight_arr = []
    total_words = sum([int(item[1]) for item in listogram])
    for hist in listogram:
        weight_arr.append([hist[0], hist[1]/total_words])
    return weight_arr

def cum_weight_hist(histogram):
    """ Return the total tokens/frequencies in histogram"""
    cumlative_arr = []
    total_words = sum([int(item[1]) for item in sample])
    for word in histogram:
        print(word)

def population(histogram, pop_size):
    """ Get the frequency of histogram words in a certian population"""
    pop_dict = {}
    for _ in range(pop_size):
        word = stochastic_sampling(histogram)
        if word in pop_dict:
            pop_dict[word] +=1
        else:
            pop_dict[word] = 1
    return pop_dict.keys()

if __name__ =="__main__":
    text = handle_input(sys.argv[1])
    histogram = Histogram(text)
    text = handle_input(sys.argv[1])
    print(histogram.frequency("this"))
    print(histogram.sort('word'))
    print(histogram.sort('count'))
    weighted_arr = weighted_hist(histogram.tuple)
    print(population(weighted_arr, 4))
    cum_weight_hist(histogram)
