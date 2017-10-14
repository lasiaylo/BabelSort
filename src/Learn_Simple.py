'''
Created on Oct 14, 2017

@author: lasia lo
'''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

genres = ['a','b','c','d','e']

#need to get the batches of text


#need to find way to embed code into numbers


#parameters

chunkLength = 100
numberOfGenres = 4
   
#Graph input
inputSample = tf.placeholder(tf.float32, [None, chunkLength]) #array size of unlimited, each array size is textLength
nodeWeight = tf.Variable(tf.zeros([chunkLength,numberOfGenres])) 
nodeBias = tf.Variable(tf.zeros[10])

# y = x * W + b
actualOutcome = tf.matmul(inputSample,nodeWeight) + nodeBias

expectedOutcome = tf.placeholder(tf.float32, [None, numberOfGenres])

crossEntropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(expectedOutcome,actualOutcome))

trainingStep = tf.train.GradientDescentOptimizer(0.5).minimize(crossEntropy)

session = tf.InteractiveSession()
tf.global_variables_initializer().run()

# Train
for _ in range(1000):
    sampleBatch, genreBatch = 
    sess.run(trainingStep,{sampleBatch, genreBatch})

# Testing
correctPrediction = tf.equal(tf.argmax(actualOutcome,1), tf.argmax(expectedOutcome,1))
accuracy = tf.reduce_mean(tf.cast(correctPrediction, tf.float32))

print(session.run(accuracy,{testinput,testlabels}))

