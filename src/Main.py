'''
Created on Oct 14, 2017

@author: lasia lo
'''
import Learn_Simple
import book_parse
import tf_glove

parser = book_parse.BookParser()
fileNames = parser.get_fnames('Data Sets\Fantasy','.epub')

lines = parser.book_parse(fileNames[0])
lines = parser.list_parser(lines, 10)
model = tf_glove.GloVeModel(embedding_size=10,context_size=2)
model.fit_to_corpus(lines)
model.train(num_epochs=20)
print(model.embeddings)
model.generate_tsne()



# learn = Learn_Simple.Learn([3],[2],[3],[2])
