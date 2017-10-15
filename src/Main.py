'''
Created on Oct 14, 2017

@author: lasia lo
'''
import Learn_Simple
import book_parse



parser = book_parse.BookParser()
fileNames = parser.get_fnames('Data Sets\Fantasy','.epub')
for x in fileNames:
    print(x)

# learn = Learn_Simple.Learn([3],[2],[3],[2])
