import zipfile
import os
import string
from bs4 import BeautifulSoup

word_dictionary = {}
curr_dir = os.getcwd()

def book_parse(fname):
    print(fname)
    book_text = []
    base_fname = os.path.splitext(fname)[0]
    # creates a folder with name of book
    extract_epub(fname, base_fname)
    chapter_list = get_fnames(base_fname, ".xhtml")[0:-1]

    os.chdir(os.path.join(curr_dir, base_fname))
    for chapter in chapter_list:
        chapter_text = extract_xhtml(chapter)
        chapter_text = remove_punc(chapter_text)
        chapter_text = chapter_text.split()
        book_text = book_text + chapter_text
    os.chdir(curr_dir)

    return book_text

def extract_epub(fname, end_dir):
    with zipfile.ZipFile(fname, "r") as myzip:
        myzip.extractall(os.path.join(curr_dir, end_dir))

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

def get_fnames(directory, ftype):
    ftype_list = []
    for file in os.listdir(os.path.join(curr_dir, directory)):
        if file.endswith(ftype):
            ftype_list.append(file)
    return ftype_list

def remove_punc(text):
    exclude = set(string.punctuation)
    text = ''.join(char for char in text if char not in exclude)
    return text

# print(get_fnames("Extracted Files", ".xhtml"))
# print(book_list)

# book_list = get_fnames("", ".epub")
#
# for book in book_list:
#     print(book_parse(book)[:100])
