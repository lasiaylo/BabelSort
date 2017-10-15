'''
Created on Oct 14, 2017

@author: lasia lo
'''
import Learn_Simple
import book_parse
import tf_glove
import numpy as np

parser = book_parse.BookParser()

#fantasy
fileNames = parser.get_fnames('Data Sets\Fantasy','.epub')
lines = parser.book_parse(fileNames[0])
lines = parser.list_parser(lines, 1000)
lines = lines[0:50]
 
model = tf_glove.GloVeModel(embedding_size=250,context_size=4)
model.fit_to_corpus(lines)
model.train(num_epochs=5)
trainInput = model.embeddings
trainInput = trainInput[0:1000]


trainGenre = [[1,0,0,0,0]] * 1000

print(len(trainInput))
print("2")
fileNames = parser.get_fnames('Data Sets\History','.epub')
lines = parser.book_parse(fileNames[0])
lines = parser.list_parser(lines, 1000)
lines = lines[0:50]
 
model = tf_glove.GloVeModel(embedding_size=250,context_size=4)
model.fit_to_corpus(lines)
model.train(num_epochs=5)
trainInput2 = model.embeddings
trainInput2 = trainInput2[0:1000]
trainInput = np.append([trainInput] , [trainInput2],axis=1)
trainInput = trainInput[0]
trainGenre = trainGenre+[[0,1,0,0,0]] * 1000
print(len(trainInput))

print("3")
fileNames = parser.get_fnames('Data Sets\Literature','.epub')
lines = parser.book_parse(fileNames[0])
lines = parser.list_parser(lines, 1000)
lines = lines[0:50]
 
model = tf_glove.GloVeModel(embedding_size=250,context_size=4)
model.fit_to_corpus(lines)
model.train(num_epochs=5)
trainInput2 = model.embeddings
trainInput2 = trainInput2[0:1000]

trainInput = np.append([trainInput] , [trainInput2],axis=1)
trainInput = trainInput[0]

trainGenre = trainGenre+[[0,0,1,0,0]] * 1000

print(len(trainInput))
print("4")
fileNames = parser.get_fnames('Data Sets\Science','.epub')
lines = parser.book_parse(fileNames[0])
lines = parser.list_parser(lines, 1000)
lines = lines[0:50]
 
model = tf_glove.GloVeModel(embedding_size=250,context_size=4)
model.fit_to_corpus(lines)
model.train(num_epochs=5)
trainInput2 = model.embeddings
trainInput2 = trainInput2[0:1000]

trainInput = np.append([trainInput] , [trainInput2],axis=1)
trainInput = trainInput[0]

trainGenre = trainGenre+[[0,0,0,1,0]] * 1000

print(len(trainInput))
print("5")
fileNames = parser.get_fnames('Data Sets\Science Fiction','.epub')
lines = parser.book_parse(fileNames[0])
lines = parser.list_parser(lines, 1000)
lines = lines[0:50]
 
model = tf_glove.GloVeModel(embedding_size=250,context_size=4)
model.fit_to_corpus(lines)
model.train(num_epochs=5)
trainInput2 = model.embeddings
trainInput2 = trainInput2[0:1000]

trainInput = np.append([trainInput] , [trainInput2],axis=1)
trainInput = trainInput[0]

trainGenre = trainGenre+[[0,0,0,0,1]] * 1000
print(len(trainInput))
print(len(trainGenre))

print("Now Creating Testcase")
fileNames = parser.get_fnames('Data Sets\History','.epub')
lines = parser.book_parse(fileNames[2])
lines = parser.list_parser(lines, 1000)
lines = lines[0:50]
 
model2 = tf_glove.GloVeModel(embedding_size=250,context_size=4)
model2.fit_to_corpus(lines)
model2.train(num_epochs=5)
testInput = model2.embeddings

testInput = (trainInput[0:1000])  
testGenre = [[0,1,0,0,0]] * 1000

print(len(testInput))
print(len(testGenre))

#  
# lines2 = parser.book_parse(fileNames[1])
# lines2 = parser.list_parser(lines2, 1000)
# lines2 = lines2[0:50]
# model2 = tf_glove.GloVeModel(embedding_size=250,context_size=2)
# model2.fit_to_corpus(lines2)
# model2.train(num_epochs=5)
# testInput = model2.embeddings
# testInput = testInput[0:1000]
# testGenre = [[0,1]] * 1000
print("now starting formal training")
# trainInput = numpy.array([[0,1,2,3,4],[0,1,4,4,4]])
# trainGenre = numpy.array([[0,1],[0,1]])
# testInput = numpy.array([[0,1,2,3,4],[0,1,2,3,4]])
# testGenre = numpy.array([[0,1],[0,1]])
# 
learn = Learn_Simple.Learn(trainInput,trainGenre,testInput,testGenre)
