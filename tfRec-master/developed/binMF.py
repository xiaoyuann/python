import tensorflow as tf
import numpy as np
import pandas as pd
from baseMF import  baseMF
from BMF import  BMF

import time
from collections import deque
from regression import regressionModel


class binMF(BMF):
    def __init__(self, K=100, component = 10, lambd = 0.01,reg=0.001,learningRate=0.005, batchSize=1024, epochs=20, users=6041, items=3953,
                 minRating=1., maxRating=5.,mod = 'Linear'):
        #
        super(binMF, self).__init__(K, reg, learningRate, batchSize, epochs, users, items, minRating, maxRating)
        self.regression = regressionModel(_mod=mod)


    def buildGraph(self):
        userWeightBatch = tf.nn.softmax(tf.nn.embedding_lookup(self.userWeight, self.userBatch))
        itemWeightBatch = tf.nn.softmax(tf.nn.embedding_lookup(self.itemWeight, self.itemBatch))
        #userWeightBatch = tf.nn.relu(tf.nn.embedding_lookup(self.userWeight, self.userBatch))
        #itemWeightBatch = tf.nn.relu(tf.nn.embedding_lookup(self.itemWeight, self.itemBatch))

        #userBiasBatch = tf.nn.embedding_lookup(self.userBias, self.userBatch)
        #itemBiasBatch = tf.nn.embedding_lookup(self.itemBias, self.itemBatch)

        prediction = tf.reduce_sum(self.regression(tf.multiply(userWeightBatch, itemWeightBatch)),1)

        #output = tf.add(output, self.globalBias)
        #output = tf.add(output, userBiasBatch)
        #prediction = tf.add(output, itemBiasBatch)

        base = tf.nn.l2_loss(tf.subtract(prediction, self.ratingBatch))
        reg = self.reg * tf.add(tf.nn.l2_loss(userWeightBatch), tf.nn.l2_loss(itemWeightBatch))
        cost = tf.add(base, reg)
        return prediction, cost


