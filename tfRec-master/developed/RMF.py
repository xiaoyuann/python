import tensorflow as tf
import numpy as np
import pandas as pd
from BMF import  BMF
import time
from collections import deque
from regression import regressionModel

class RMF(BMF):
    def __init__(self, K=5, criteriaNum = 3, reg=0.001, lambd = 0.01,learningRate=0.005, batchSize=1024, epochs=20, users=6041, items=3953,
                 minRating=1., maxRating=5.,mod = 'Linear'):
        #criteriaNum mean the Number of sub-criteria/subrating
        #super(RMF, self).__init__(K, reg, learningRate, batchSize, epochs, users, items, minRating, maxRating)
        self.K = K
        self.reg = reg
        self.criteriaNum = criteriaNum + 1
        self.lambd = lambd
        self.learningRate = learningRate
        self.batchSize = batchSize
        self.epochs = epochs
        self.users = users
        self.items = items
        self.minRating = minRating
        self.maxRating = maxRating

        self.globalBias = tf.Variable(tf.zeros([self.criteriaNum]))
        self.userBias = tf.Variable(tf.zeros([self.users,self.criteriaNum]))
        self.itemBias = tf.Variable(tf.zeros([self.items,self.criteriaNum]))
        self.userBatch = tf.placeholder(tf.int32, [None], name='userBatch')
        self.itemBatch = tf.placeholder(tf.int32, [None], name='itemBatch')
        self.ratingBatch = tf.placeholder(tf.float32, [None,self.criteriaNum], name='ratingBatch')
        self.userWeight = tf.Variable(tf.random_normal([self.users, self.K,self.criteriaNum]) / np.sqrt(self.users))
        self.itemWeight = tf.Variable(tf.random_normal([self.items, self.K,self.criteriaNum ]) / np.sqrt(self.items))
        self.init = False

        self.regression = regressionModel(_mod = mod,reg = self.reg)

    def getData(self, train=None, test=None, ignore=False,):
        m = train.max() + 1
        if (not ignore) and (m[0] != self.users):
            print(
                'error: the user num [%d] is not equal the maximum user ID [%d] in data,please check or setting ignore=True' % (
                    self.users, m[0]))
            #return
        if (not ignore) and (m[1] != self.items):
            print(
                'error: the item num [%d] is not equal the maximum item ID [%d] in data,please check or setting ignore=True' % (
                    self.items, m[1]))
            #return
        self.trainData = train.values[:, :2 + self.criteriaNum ]
        self.testData = test.values[:, :3]
        self.trRow = self.trainData.shape[0]
        self.tsRow = self.testData.shape[0]

    def buildGraph(self):
        userWeightBatch = tf.nn.embedding_lookup(self.userWeight, self.userBatch)
        itemWeightBatch = tf.nn.embedding_lookup(self.itemWeight, self.itemBatch)
        userBiasBatch = tf.nn.embedding_lookup(self.userBias, self.userBatch)
        itemBiasBatch = tf.nn.embedding_lookup(self.itemBias, self.itemBatch)
        output = tf.reduce_sum(tf.multiply(userWeightBatch, itemWeightBatch), 1)
        output = tf.add(output, self.globalBias)
        output = tf.add(output, userBiasBatch)
        subPrediction = tf.add(output, itemBiasBatch)
        #subPrediction = tf.clip_by_value(subPrediction, self.minRating, self.maxRating)
        subCost = self.lambd * tf.nn.l2_loss(tf.subtract(subPrediction, self.ratingBatch))
        reg = self.reg * tf.add(tf.nn.l2_loss(userWeightBatch), tf.nn.l2_loss(itemWeightBatch))
        prediction =  self.regression(subPrediction)
        globalCost = tf.nn.l2_loss(tf.subtract(prediction, self.ratingBatch[:,0]))
        #globalCost = tf.nn.log_poisson_loss( tf.reshape(self.ratingBatch[:,0],-1),prediction)
        base = tf.add(subCost, globalCost)
        cost = tf.add(base, reg)
        return prediction, cost

