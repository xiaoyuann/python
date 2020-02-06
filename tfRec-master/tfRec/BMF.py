import tensorflow as tf
import numpy as np
#import pandas as pd
from baseMF import baseMF
import time
#import matplotlib.pyplot as plt
# from remtime import *
from collections import deque


# from remtime import printTime
class BMF(baseMF):
    # def __init__(self, K=5, reg=0.001, learningRate=0.005, batchSize=512, epochs=20, users=6041, items=3953,
    #                 minRating=1., maxRating=5., optimizer ='sgd'):
    def __init__(self, biasReg=0.01, **kwargs):
        # super(BMF, self).__init__(K, reg, learningRate, batchSize, epochs, users, items, minRating, maxRating,optimizer)
        super(BMF, self).__init__(**kwargs)
        # self.userBias = tf.Variable(tf.random_normal([self.users],stddev = 0.1))
        # self.itemBias = tf.Variable(tf.random_normal([self.items],stddev = 0.1))
        # super(BMF, self).__init__(**kwargs)
        self.biasReg = biasReg
        # self.globalBias = tf.Variable(tf.zeros([]))
        self.userBias = tf.Variable(tf.zeros([self.users]))
        self.itemBias = tf.Variable(tf.zeros([self.items]))

    def buildGraph(self):
        # userBatch, itemBatch, ratingBatch = it.get_next()
        self.globalBias = tf.constant(self.trainData[:, 2:3].mean(axis=0), dtype=tf.float32)
        userWeightBatch = tf.nn.embedding_lookup(self.userWeight, self.userBatch)
        itemWeightBatch = tf.nn.embedding_lookup(self.itemWeight, self.itemBatch)

        userBiasBatch = tf.nn.embedding_lookup(self.userBias, self.userBatch)
        itemBiasBatch = tf.nn.embedding_lookup(self.itemBias, self.itemBatch)

        output = tf.reduce_sum(tf.multiply(userWeightBatch, itemWeightBatch), 1)

        output = tf.add(output, self.globalBias)
        output = tf.add(output, userBiasBatch)
        prediction = tf.add(output, itemBiasBatch)

        base = tf.nn.l2_loss(tf.subtract(prediction, self.ratingBatch))
        # base = tf.nn.l2_loss(tf.nn.sigmoid(tf.subtract(prediction, self.ratingBatch)))
        # reg = self.reg * tf.add(tf.nn.l2_loss(userWeightBatch), tf.nn.l2_loss(itemWeightBatch))
        reg = tf.add(self.uReg * tf.nn.l2_loss(userWeightBatch), self.iReg * tf.nn.l2_loss(itemWeightBatch))

        bReg = tf.add(tf.nn.l2_loss(self.biasReg * userBiasBatch), tf.nn.l2_loss(self.biasReg * itemBiasBatch))
        # bReg = tf.add(bReg, tf.nn.l2_loss(self.globalBias))
        reg = tf.add(reg, bReg)
        cost = tf.add(base, reg)
        # r = tf.clip_by_value(prediction,self.minRating,self.maxRating)
        # error = tf.reduce_mean(tf.pow(tf.subtract(r, self.ratingBatch),2))
        # print ('OK')
        return prediction, cost  # ,error


# if __name__ == '__main__':
#     dataset = 'ta'
#     cv = 10
#     train = pd.read_csv('datasets/%s.cv%d.base' % (dataset, cv), sep='\t', header=None)
#     test = pd.read_csv('datasets/%s.cv%d.test' % (dataset, cv), sep='\t', header=None)
#     # A = BMF(items = 7045,users = 920,epochs=100,reg =  0.1,learningRate=0.001,batchSize=128)
#     #A = BMF(items=35620, users=1412, epochs=1500, reg=0.1, learningRate=0.005, batchSize=128)
#     A = BMF(items= 3469, users = 1653, epochs=50, iReg =  0.1, uReg = 0.01, learningRate=0.01, batchSize=1, optimizer = 'sgd')
#     A.getData(train=train, test=test)
#     A.train()
