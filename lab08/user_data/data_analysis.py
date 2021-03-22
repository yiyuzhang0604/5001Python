# Name: Yiyu Zhang
# Github: https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-YiyuZhang
import re


class DataAnalysis:
    def __init__(self, file):
        self.lang = []
        # TODO: set up the necessary instance variables
        self.count = 0
        self.emails = ''
        self.domains = []
        self.df = self.read_data(file)
        # type of df: string

    def get_domain(self, email):
        """ get the 2-letter domain in each email"""
        res = email.split(".")
        if (len(res[-1]) == 2):
            if res[-1] not in self.domains:
                self.domains.append(res[-1])
            self.emails += (' ' + res[-1])

    def read_data(self, file_name):
        # TODO: read the data and get the counts
        try:
            f = open(file_name, "r")
        except FileNotFoundError as e:
            print("Can't open", file_name)
            return
        for line in f.readlines():
            words = line.split(",")
            self.count += 1
            email = words[3]
            self.get_domain(email)
            lan = words[-1].rstrip('\n')
            self.lang.append(lan)
        self.count -= 1
        # need to open the file again to retrieve the data
        try:
            f = open(file_name, "r")
        except FileNotFoundError as e:
            print("Can't open", file_name)
            return
        return f.read()
        # the type of f.read(): string

    # TODO:
    # Implement top_n_lang_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing languages
    # and their frequencies in the data, ordered from
    # highest frequency to lowest.
    def top_n_lang_freqs(self, n):
        dic = {}
        """ number -> n-length list of tuples represent language"""
        for language in self.lang:
            dic[language] = len(re.findall(language, self.df))/self.count
        data = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return data[:n]

    # TODO:
    # Implement top_n_country_tlds_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing country (2-letter)
    # top-level domain identifiers (e.g. 'jp', 'uk', 'cn', 'ca')
    # and their frequencies as email domains the data, ordered
    # from highest frequency to lowest.
    def top_n_country_tlds_freqs(self, n):
        """ number -> n-length list of tuples represent country"""
        dic = {}
        for dom in self.domains:
            dic[dom] = len(re.findall(dom, self.emails))/self.count

        data = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return data[:n]
    # TODO:
    # Implement any other necessary/helpful methods to support
    # the ones above.
