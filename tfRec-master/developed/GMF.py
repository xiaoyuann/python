__author__ = 'FanGhost'
__date__ = '4/10/2018'

import tensorflow as tf
import numpy as np
import pandas as pd
from baseMF import baseMF
import time
from regression import regressionModel

class GMF(baseMF):
    def __init__(self,mod = 'Linear',regressionReg=0.01, **kwargs):
        #criteriaNum mean the Number of sub-criteria/subrating
        super(GMF, self).__init__(**kwargs)
        self.regressionReg = regressionReg
        self.regrission  = regressionModel(_mod = mod,reg=regressionReg)

    def buildGraph(self):
        #self.globalBias = tf.constant(self.trainData[:, 2:3].mean(axis=0), dtype=tf.float32)
        userWeightBatch = tf.nn.embedding_lookup(self.userWeight, self.userBatch)
        itemWeightBatch = tf.nn.embedding_lookup(self.itemWeight, self.itemBatch)
        #userWeightBatch = tf.nn.softmax(tf.nn.embedding_lookup(self.userWeight, self.userBatch))
        #itemWeightBatch = tf.nn.softmax(tf.nn.embedding_lookup(self.itemWeight, self.itemBatch))
        outputs = tf.multiply(userWeightBatch, itemWeightBatch)
        #prediction = tf.add(self.globalBias,outputs)
        do = tf.nn.dropout(outputs,keep_prob= 0.5)
        prediction = self.regrission(do)
        base = tf.nn.l2_loss(tf.subtract(prediction, self.ratingBatch))
        reg = tf.add(self.uReg * tf.nn.l2_loss(userWeightBatch), self.iReg * tf.nn.l2_loss(itemWeightBatch))
        wreg = self.regressionReg*tf.nn.l2_loss(self.regrission.weights[0]) #l2 reg
        #wreg = self.regressionReg * tf.reduce_sum(abs(self.regrission.weights[0]),1) #l1 reg
        cost = tf.add(base, reg)
        cost = tf.add(cost, wreg)
        return prediction, cost

if __name__ == '__main__':
    dataset = 'ta'
    cv = 10
    train = pd.read_csv('datasets/%s.cv%d.base' % (dataset, cv), sep='\t', header=None)
    test = pd.read_csv('datasets/%s.cv%d.test' % (dataset, cv), sep='\t', header=None)
    A = GMF(K=50,items = 3469,users = 1653,epochs=5000,iReg =  0.1, uReg = 0.1,regressionReg=1, learningRate=0.0001,batchSize=128,optimizer = 'adam')
    #A = GMF(items=35620, users=1412, epochs=1500, reg=0.1, learningRate=0.005, batchSize=128)
    A.getData(train=train, test=test)
    A.train()



