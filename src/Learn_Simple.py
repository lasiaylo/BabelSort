'''
Created on Oct 14, 2017

@author: lasia lo
'''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np
import random

class Learn(object):
    '''
    Simple neural network - one layer
    '''


    def __init__(self, trainTexts,trainGenres,testInput,testGenre):
        '''
        Constructor
        '''
        #Graph input
        #parameters
        CHUNKLENGTH = 1000
        NUMBEROFGENRES = 5
        trainTexts = np.array(trainTexts)
        trainGenres = np.array(trainGenres)
    
        
        inputSample = tf.placeholder(tf.float32, [None, CHUNKLENGTH], name = 'sup') #array size of unlimited, each array size is textLength
        nodeWeight = tf.Variable(tf.zeros([CHUNKLENGTH,NUMBEROFGENRES])) 
        nodeBias = tf.Variable(tf.zeros([NUMBEROFGENRES]))

        # y = x * W + b
        actualOutcome = (tf.matmul(inputSample,nodeWeight) + nodeBias)
        
        expectedOutcome = tf.placeholder(tf.float32, [None, NUMBEROFGENRES])
        
        
        crossEntropy = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits(labels=expectedOutcome,logits=actualOutcome))
        
        trainingStep = tf.train.GradientDescentOptimizer(.5).minimize(crossEntropy)
        
        session = tf.InteractiveSession()
        
        tf.global_variables_initializer().run()
        
        # Train
        for step in range(len(trainTexts)):
#             step =random.randint(0,len(trainTexts)-1)
            sampleBatch = [trainTexts[step]]
            genreBatch = [trainGenres[step]]
#             if (step%200 == 0):
#                 correctPrediction = tf.equal(tf.argmax(actualOutcome,1), tf.argmax(expectedOutcome,1))
#                 accuracy = tf.reduce_mean(tf.cast(correctPrediction, tf.float32))
#                 print(session.run(accuracy, feed_dict={inputSample: testTexts,expectedOutcome: testGenres}))
            session.run(trainingStep, feed_dict={inputSample: sampleBatch,expectedOutcome:genreBatch})
        
#         self.session = session
#         self.actualOutcome = actualOutcome
#         self.expectedOutcome = expectedOutcome
#         self.inputSample = inputSample
        
#     def test(self,testTexts,testGenres):
        testTexts = np.array(testInput)
        testGenres = np.array(testGenre)
        correctPrediction = tf.equal(tf.argmax(actualOutcome,1), tf.argmax(expectedOutcome,1))
        accuracy = tf.reduce_mean(tf.cast(correctPrediction, tf.float32))
        print(session.run(accuracy, feed_dict={inputSample: testTexts,expectedOutcome: testGenres}))
        
