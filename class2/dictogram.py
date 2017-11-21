#!python
from __future__ import division, print_function  # Python 2 and 3 compatibility
from pprint import pprint
import time


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        if word in self:
            self[word] += count
        else:
            self.types +=1 
            self[word] = count
        self.tokens += count
        print(self)

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        if word in self:
            print("{}: {}".format(word, self[word]))
            return self[word]
        else:
            return 0
    def unique_words(self):
        """ Return words that have a value of one """
        return [key for key, val in self.item() if val==1] 

    def export_histogram(self, histogram_title):
        """ Create a text file of histogram based on file name """
        file =  open(histogram_title+'.txt', 'w')
        for key, val in self.items():
            string = "{} {}\n".format(key,val)
            file.write(string)
        file.close()

    def weighted_hist(self):
        """Return a dictionary with value equal to value/tokens"""
        total = sum([val for val in self.values()])
        print("The total is {}".format(total))
        weight_dict = {}
        for key,val in self.items():
            weight_dict[key] = val/total
        return weight_dict

def time_diffrence(start_time):
    """ Returns the time diffrence between the start and time the function is called """ 
    return time.time()-start_time

def read_file(file_name):
    """ Read in text files based on file name """
    with open(file_name) as f:
        return f.read().split()

def handle_input(input_word):
    """ Determine whether file is a text file or a string from the system arguments """
    if input_word.endswith('.txt'):
        print('input a text file:' + input_word)
        source_text = read_text(input_word)
        print(source_text)
        return source_text
    else:
        print("input raw string \n")
        return input_word.split()


class Markov(dict):
    """Markov is a dictionary of key(current word), val/next_word(dictogram)."""
    def __init__(self, text=None):
        if text:
            self.markov(text)

    def markov(self,text):
        """ Create a markoff model based on the text array input into the file """
        x = 0
        #self['start'] += text[0] 
        while x< len(text)-1:
            word = text[x]
            next_word = text[x+1]
            if word not in self.keys():
                self[word]= Dictogram()
            self[word].add_count(next_word)
            x+=1
            
    def weight_markov(self):
        """ Return a key with a value of possible next words weighte """
        markov_weight = {}
        for key, val in self.items():
            markov_weight[key] = val.weighted_hist()
        return markov_weight
    def generate_sentence(self, length):
        """Return a sentence""" 
        x = 0
        while x< length:
            pass


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())
        marky = Markov("one fish two fish red fish blue fish".split())
        print(marky)
        pprint(marky.weight_markov())

if __name__ == '__main__':
    main()