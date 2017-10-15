'''
Created on Oct 14, 2017

@author: lasia
'''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import tempfile

import tensorflow as tf

CHUNKLENGTH = 100
CHUNKDIMENSION = CHUNKLENGTH ** (.5)
NUMBEROFGENRES = 4

inputSample = tf.placeholder(tf.float32, [None, CHUNKLENGTH],name = 'x') #array size of unlimited, each array size is textLength
nodeWeight = tf.Variable(tf.zeros([CHUNKLENGTH,NUMBEROFGENRES]),name = 'weights') 
nodeBias = tf.Variable(tf.zeros[10], name = 'biases')
def deepnn(x):
    with tf.name_scope('reshape'):
        inputImage = tf.reshape(inputSample,[-1,CHUNKDIMENSION,CHUNKDIMENSION,1])
    
    with tf.name_scope('conv1'):
        W_conv1 = weight_variable([5,5,1,32])
        b_conv1 = bias_variable([32])