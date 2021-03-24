from text_cleaner import TextCleaner
import re


class NgramFrequencies:
    def __init__(self, string, n):
        self.dict = {}
        self.freq = {}
        self.count = 0
        self.total_count = 0
        self.list = []

    def add_item(self, ngram):
        """ takes an n-gram and increments its count in the dict"""
        if ngram in self.dict.keys():
            self.dict[ngram] += 1
        else:
            self.dict[ngram] = 1
            self.count += 1
        return self.dict

    def get_list(self, text_string, n):
        new = re.findall(r"([^\s]+)", text_string)
        if n == 1:
            for i in range(len(new)):
                uni = new[i]
                self.list.append(uni)
                self.add_item(uni)
                self.total_count += 1
        if n == 2:
            for i in range(len(new) - 1):
                bi = '_'.join(new[i: i + n])
                self.list.append(bi)
                self.add_item(bi)
                self.total_count += 1
        if n == 3:
            for i in range(len(new) - 2):
                tri = '_'.join(new[i: i + n])
                self.list.append(tri)
                self.add_item(tri)
                self.total_count += 1

    def top_n_counts(self, n):
        """ return a list of items sorted on the count, reverse = true"""
        data = sorted(self.dict.items(), key=lambda x: x[1], reverse=True)
        return data[:n]

    def frequency(self, word):
        """ takes an item and returns its frequency"""
        count = self.dict[word]
        total = self.total_count
        frequency = round((count/total), 3)
        return frequency

    def top_n_freqs(self, n):
        """ return a similar list, but with frequency instead of counts"""
        for word in self.dict:
            self.freq[word] = self.frequency(word)
        data = sorted(self.freq.items(), key=lambda x: x[1], reverse=True)
        return data[:n]
