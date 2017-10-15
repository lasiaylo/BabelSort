'''
Created on Oct 14, 2017

@author: lasia lo
'''
import Learn_Simple
import book_parse
import tf_glove
import numpy as np

parser = book_parse.BookParser()
learn = Learn_Simple.Learn()

#fantasy

fileNames = parser.get_fnames('Data Sets\Fantasy','.epub')
lines = parser.book_parse(fileNames[0])
lines = parser.list_parser(lines, 1000)
lines = lines[0:50]

model = tf_glove.GloVeModel(embedding_size=250,context_size=4)
model.fit_to_corpus(lines)
model.train(num_epochs=5)
trainInput = model.embeddings
trainInput = trainInput[0:3000]

trainGenre = [[1,0,0,0,0]] * 3000

print("now starting training")
learn.train(trainInput,trainGenre)

fileNames = parser.get_fnames('Data Sets\Fantasy','.epub')
lines = parser.book_parse(fileNames[1])
lines = parser.list_parser(lines, 1000)
lines = lines[0:50]

model = tf_glove.GloVeModel(embedding_size=250,context_size=4)
model.fit_to_corpus(lines)
model.train(num_epochs=5)
testInput = model.embeddings
testInput = trainInput[0:3000]
testGenre = [[1,0,0,0,0]] * 3000

print("now starting testing")
learn.test(testInput,testGenre)




