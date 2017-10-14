import zipfile
import os
from bs4 import BeautifulSoup

word_dictionary = {}
curr_dir = os.getcwd()

<<<<<<< HEAD
def book_parse(fname):
    print(fname)
    book_text = []
    base_fname = os.path.splitext(fname)[0]
    # creates a folder with name of book
    extract_epub(fname, base_fname)
    chapter_list = get_fnames(base_fname, ".xhtml")


    for chapter in chapter_list:
        chapter_text = extract_xhtml(chapter)
        book_text = book_text + chapter_text

    return book_text
=======
# def book_parse(fname):
>>>>>>> parent of 87548a0... book_parse

def extract_epub(fname, end_dir):
    with zipfile.ZipFile(fname, "r") as myzip:
        myzip.extractall(os.path.join(curr_dir, end_dir))

def extract_xhtml(fname):
    with open(os.path.join(/Users/murtazaHusain/Documents/GitHub/BabelSort/[Linda_Nagata]_The_Bohr_Maker(BookZZ.org), fname)) as html_fp:
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

# print(get_fnames("Extracted Files", ".xhtml"))
<<<<<<< HEAD
# book_list = get_fnames("", ".epub")
# print(book_list)
print(book_parse("[Linda_Nagata]_The_Bohr_Maker(BookZZ.org).epub"))
=======
book_list = get_fnames("", ".epub")
print(book_list)
>>>>>>> parent of 87548a0... book_parse
