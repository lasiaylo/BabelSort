'''
Created on Oct 14, 2017

@author: lasia lo
'''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np


class Learn(object):
    '''
    Simple neural network - one layer
    '''


    def __init__(self):
        '''
        Constructor
        '''
        #Graph input
        #parameters
        CHUNKLENGTH = 250
        NUMBEROFGENRES = 5

        self.inputSample = tf.placeholder(tf.float32, [None, CHUNKLENGTH], name = 'sup') #array size of unlimited, each array size is textLength
        self.nodeWeights = tf.Variable(tf.zeros([CHUNKLENGTH,NUMBEROFGENRES])) 
        self.nodeBias = tf.Variable(tf.zeros([NUMBEROFGENRES]))

        # y = x * W + b
        self.actualOutcome = (tf.matmul(self.inputSample,self.nodeWeights) + self.nodeBias)
        
        self.expectedOutcome = tf.placeholder(tf.float32, [None, NUMBEROFGENRES])
        
        self.session = tf.InteractiveSession()
        tf.global_variables_initializer().run()
        
    def train(self, trainTexts,trainGenres):  
        self.trainTexts = np.array(trainTexts)
        self.trainGenres = np.array(trainGenres)
  
        
        self.crossEntropy = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits(labels=self.expectedOutcome,logits=self.actualOutcome))
        
        trainingStep = tf.train.GradientDescentOptimizer(0.5).minimize(self.crossEntropy)  
        
        # Train
        print(len(trainTexts))
        for step in range(len(trainTexts)):
            sampleBatch = [trainTexts[step]]
            genreBatch = [trainGenres[step]]
#             if (step%200 == 0):
#                 correctPrediction = tf.equal(tf.argmax(actualOutcome,1), tf.argmax(expectedOutcome,1))
#                 accuracy = tf.reduce_mean(tf.cast(correctPrediction, tf.float32))
#                 print(session.run(accuracy, feed_dict={inputSample: testTexts,expectedOutcome: testGenres}))
            self.session.run(trainingStep, feed_dict={self.inputSample: sampleBatch,self.expectedOutcome:genreBatch})
        
      

    def test(self,testTexts,testGenres):
        self.testTexts = np.array(testTexts)
        self.testGenres = np.array(testGenres)
        correctPrediction = tf.equal(tf.argmax(self.actualOutcome,1), tf.argmax(self.expectedOutcome,1))
        accuracy = tf.reduce_mean(tf.cast(correctPrediction, tf.float32))
        print(self.session.run(accuracy, feed_dict={self.inputSample: testTexts,self.expectedOutcome: testGenres}))
        
    def getNodeWeight(self):
        return (self.session.run(self.nodeWeights))
    def getNodeBias(self):
        return (self.session.run(self.getNodeBias))
