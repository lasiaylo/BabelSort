'''
Created on Oct 14, 2017

@author: lasia lo
'''
import Learn_Simple
import book_parse
import tf_glove

parser = book_parse.BookParser()
learn = Learn_Simple.Learn()
def setTrainGenre(fileNames,trainGenre):
    x = 0
    for file in fileNames:
        lines = parser.book_parse(file)
        lines = parser.list_parser(lines, 1000)
        lines = lines[0:50]
        
        model = tf_glove.GloVeModel(embedding_size=250,context_size=4)
        model.fit_to_corpus(lines)
        model.train(num_epochs=5)
        trainInput = model.embeddings
        
        trainInput = trainInput[0:3000]
        
        learn.train(trainInput,trainGenre)
        x +=1
        if x ==3:
            break
        
#fantasy
print("Scanning Fantasy")
fileNames = parser.get_fnames('Data Sets\Fantasy','.epub')
trainGenre = [[1,0,0,0,0]] * 3000
setTrainGenre(fileNames,trainGenre)

print("Scanning History")
fileNames = parser.get_fnames('Data Sets\History','.epub')
trainGenre = [[0,1,0,0,0]] * 3000
setTrainGenre(fileNames,trainGenre)

print("Scanning Literature")
fileNames = parser.get_fnames('Data Sets\Literature','.epub')
trainGenre = [[0,0,1,0,0]] * 3000
setTrainGenre(fileNames,trainGenre)

print("Scanning Science")
fileNames = parser.get_fnames('Data Sets\Science','.epub')
trainGenre = [[0,0,0,1,0]] * 3000
setTrainGenre(fileNames,trainGenre)

print("Scanning Sci-Fi")
fileNames = parser.get_fnames('Data Sets\Science Fiction','.epub')
trainGenre = [[0,0,0,0,1]] * 3000
setTrainGenre(fileNames,trainGenre)
        
        

    
    
fileNames = parser.get_fnames('Data Sets\Fantasy\Test Files','.epub')
    
lines = parser.book_parse(fileNames[1])
lines = parser.list_parser(lines, 1000)
lines = lines[0:50]

model = tf_glove.GloVeModel(embedding_size=250,context_size=4)
model.fit_to_corpus(lines)
model.train(num_epochs=5)
testInput = model.embeddings
testInput = testInput[0:3000]
testGenre = [[1,0,0,0,0]] * 3000


print("now starting testing")
learn.test(testInput,testGenre)




