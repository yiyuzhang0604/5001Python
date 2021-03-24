import sys
import re
from ngrams import NgramFrequencies
from text_cleaner import TextCleaner


def main(file_name):
    # pre-processing
    try:
        f = open(file_name, "r")
    except FileNotFoundError as e:
        print("Can't open", file_name)
        return
    text_string = f.read()
    cleaner = TextCleaner(text_string)
    lower = cleaner.convert_to_lower(text_string)
    no_punct = cleaner.no_puntuation(lower)

    # report for unigram
    uni = NgramFrequencies(no_punct, 1)
    uni.get_list(no_punct, 1)
    print("Top 10 unigrams:")
    print_output(uni.top_n_freqs(10))

    # report for bigram
    bi = NgramFrequencies(no_punct, 2)
    bi.get_list(no_punct, 2)
    print("Top 10 bigrams:")
    print_output(bi.top_n_freqs(10))

    # report for trigram
    tri = NgramFrequencies(no_punct, 3)
    tri.get_list(no_punct, 3)
    print("Top 10 trigrams:")
    print_output(tri.top_n_freqs(10))


def print_output(collection):
    for item in collection:
        print((item[0], round(item[1], 3)))


main(sys.argv[1])
