import zipfile
from bs4 import BeautifulSoup

word_dictionary = {}

# def book_parse(fname):

def extract_epub(fname):
    with zipfile.ZipFile(fname, "r") as myzip:
        myzip.extractall("/Users/murtazaHusain/Desktop/Murtaza/Georgia Tech/HackGT4/Extracted Files")

# extract_epub("[Linda_Nagata]_The_Bohr_Maker(BookZZ.org).epub")

def extract_xhtml(fname):
    with open(fname) as html_fp:
        chapter = BeautifulSoup(html_fp, "html.parser")

    raw_text = chapter.get_text()
    return raw_text

raw_text = extract_xhtml("index_split_002.xhtml")

def text_to_dict(text):
    words = text.split()
    for word in words:
        if word in word_dictionary:
            word_dictionary[word] = word_dictionary[word] + 1
        else:
            word_dictionary[word] = 1
