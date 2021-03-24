import re


class TextCleaner:
    """ clean the text"""
    def __init__(self, text_string):
        self.string = text_string

    def no_puntuation(self, line):
        my_string = line
        abbrs = ['Mr.', 'Dr.', 'Ms.']
        for abbr in abbrs:
            my_string = my_string.replace(abbr, abbr[:-1])
        my_string = my_string.replace(",", " COMMA")
        my_string = my_string.replace("-", "")
        my_string = my_string.replace('"', "")
        return my_string

    def convert_to_lower(self, line):
        line = line.lower()
        return line
