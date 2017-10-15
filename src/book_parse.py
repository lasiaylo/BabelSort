import zipfile
import os
import string
import re
import epub_conversion
from epub_conversion.utils import open_book, convert_epub_to_lines
from bs4 import BeautifulSoup

class BookParser(object):
    def __init__(self):
        self.curr_dir = os.getcwd()


    def book_parse(self, fname):
        os.chdir(self.babel_dir)
        book = open_book(fname)
        lines = convert_epub_to_lines(book)
        lines = ''.join(lines)
        lines = self.remove_punc(self.cleanhtml(lines))
        lines = lines.split()
        return lines

    def cleanhtml(self, raw_html):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html)
        return cleantext

    def remove_punc(self, text):
        exclude = set(string.punctuation)
        text = ''.join(char for char in text if char not in exclude)
        return text

    def get_fnames(self, directory, ftype):
        ftype_list = []
        babel_dir = self.curr_dir.rsplit("\\", 1)[0]
        babel_dir = os.path.join(babel_dir,directory)
        for file in os.listdir(babel_dir):
            if file.endswith(ftype):
                ftype_list.append(file)
        self.babel_dir = babel_dir
        return ftype_list

    def list_parser(self, word_list, group_size):
        grouped_words = []
        temp_group = [""] * group_size
        count = 0

        for word in word_list:
            if count == group_size:
                count = 0
                grouped_words.append(temp_group)
                temp_group = [""] * group_size
            temp_group[count] = word
            count = count + 1

        grouped_words.append(temp_group)

        return grouped_words
