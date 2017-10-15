'''
Created on Oct 14, 2017

@author: lasia lo
'''
import Learn_Simple
import book_parse
import tf_glove
import numpy as np

parser = book_parse.BookParser()


def testFantasy():
    fileNames = parser.get_fnames('Data Sets\Fantasy\Test Files','.epub')
    x = 0
    for file in fileNames:
        x+=1
        
        lines = parser.book_parse(file)
        lines = parser.list_parser(lines, 2000)
        lines = lines[0:50]
        
        model = tf_glove.GloVeModel(embedding_size=1000,context_size=2)
        model.fit_to_corpus(lines)
        model.train(num_epochs=10)
        testInput = model.embeddings
        testInput = testInput[0:8000]
        testGenre = [[1,0,0,0,0]] * 8000
        
        return (testInput,testGenre)
        
       

def setTrainGenre(file,trainInput,trainGenre):
    lines = parser.book_parse(file)
    lines = parser.list_parser(lines, 2000)
    lines = lines[0:50]
    
    model = tf_glove.GloVeModel(embedding_size=1000,context_size=2)
    model.fit_to_corpus(lines)
    model.train(num_epochs=10)
    trainInput2 = model.embeddings
    trainInput2 = trainInput2[0:3000]
    
    if len(trainInput) == 0:
        return trainInput2
    trainInput = np.append([trainInput] , [trainInput2],axis=1)
    trainInput = trainInput[0]
    
    return trainInput
    
        
#fantasy
def train():
    trainInput = []
    trainGenre = []
    for index in range(10):
        print(index)
        trainInput, trainGenre = trainFantasy(index,trainInput,trainGenre)
        trainInput, trainGenre = trainHistory(index,trainInput,trainGenre)
#         trainInput, trainGenre = trainLiterature(index,trainInput,trainGenre)
#         trainInput, trainGenre = trainScience(index,trainInput,trainGenre)
#         trainInput, trainGenre = trainScienceFiction(index,trainInput,trainGenre)
    print("now training")
    testInput,testGenre = testFantasy()
    print(len(trainInput))
    print(len(trainGenre))
    learn = Learn_Simple.Learn(trainInput,trainGenre,testInput,testGenre)
    
    print("Now testing")
    
#     learn.test(testInput,testGenre)
        
        
def trainFantasy(index,trainInput,trainGenre):
    print("Training Fantasy")
    fileNames = parser.get_fnames('Data Sets\Fantasy','.epub')
    trainGenre += [[1,0,0,0,0]] * 3000
    trainInput = setTrainGenre(fileNames[index],trainInput,trainGenre)
    return (trainInput,trainGenre)

def trainHistory(index,trainInput,trainGenre):
    print("Training History")
    fileNames = parser.get_fnames('Data Sets\History','.epub')
    trainGenre += [[0,1,0,0,0]] * 3000
    trainInput = setTrainGenre(fileNames[index],trainInput,trainGenre)
    return (trainInput,trainGenre)


def trainLiterature(index,trainInput,trainGenre):
    print("Training Literature")
    fileNames = parser.get_fnames('Data Sets\Literature','.epub')
    trainGenre += [[0,0,1,0,0]] * 3000
    trainInput = setTrainGenre(fileNames[index],trainInput,trainGenre)
    return (trainInput,trainGenre)
def trainScience(index,trainInput,trainGenre):
    print("Training Science")
    fileNames = parser.get_fnames('Data Sets\Science','.epub')
    trainGenre += [[0,0,0,1,0]] * 3000
    trainInput = setTrainGenre(fileNames[index],trainInput,trainGenre)
    return (trainInput,trainGenre)
def trainScienceFiction(index,trainInput,trainGenre):
    print("Training SciFi")
    fileNames = parser.get_fnames('Data Sets\Science Fiction','.epub')
    trainGenre += [[0,0,0,0,1]] * 3000
    trainInput = setTrainGenre(fileNames[index],trainInput,trainGenre)
    return (trainInput,trainGenre)   
def readNN(fname):
    f = open(fname, "r")
    data = f.read()
    NN = [float(i) for i in data.split(",")]
    NN = np.array(NN)
    return NN

def writeNN(fname, nodeWeights):
    f = open(fname, "w")
    for i in nodeWeights:
        f.write(str(i) + " ")
# print("Writing")
# writeNN("Test1.txt",learn.getNodeWeight())


train()
    






