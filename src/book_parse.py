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


    def book_parse(fname):
        book = open_book(fname)
        lines = convert_epub_to_lines(book)
        lines = ''.join(lines)
        lines = remove_punc(cleanhtml(lines))
        lines = lines.split()
        return lines

    def cleanhtml(raw_html):
      cleanr = re.compile('<.*?>')
      cleantext = re.sub(cleanr, '', raw_html)
      return cleantext

    def remove_punc(text):
        exclude = set(string.punctuation)
        text = ''.join(char for char in text if char not in exclude)
        return text

    def get_fnames(directory, ftype):
        ftype_list = []
        babel_dir = self.curr_dir.rsplit("/", 1)[0]
        for file in os.listdir(os.path.join(babel_dir, directory)):
            if file.endswith(ftype):
                ftype_list.append(file)
        return ftype_list
