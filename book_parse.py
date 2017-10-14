import zipfile
import os
from bs4 import BeautifulSoup

word_dictionary = {}
curr_dir = os.getcwd()

# def book_parse(fname):

def extract_epub(fname):
    with zipfile.ZipFile(fname, "r") as myzip:
        myzip.extractall(os.path.join(curr_dir, "Extracted Files"))

extract_epub("[Linda_Nagata]_The_Bohr_Maker(BookZZ.org).epub")

def extract_xhtml(fname):
    with open(fname) as html_fp:
        chapter = BeautifulSoup(html_fp, "html.parser")

    raw_text = chapter.get_text()
    return raw_text

# raw_text = extract_xhtml("index_split_002.xhtml")

def text_to_dict(text):
    words = text.split()
    for word in words:
        if word in word_dictionary:
            word_dictionary[word] = word_dictionary[word] + 1
        else:
            word_dictionary[word] = 1

def get_xhtml_fnames(directory):
    xhtml_list = []
    for file in os.listdir(os.path.join(curr_dir, directory)):
        if file.endswith(".xhtml"):
            xhtml_list.append(file)
    # gets rid of titlepage.xhtml because that file doesn't have words
    xhtml_list = xhtml_list[:len(xhtml_list) - 1]
    return xhtml_list

print(get_xhtml_fnames("Extracted Files"))
