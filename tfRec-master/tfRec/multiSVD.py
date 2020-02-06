import tensorflow as tf
import time
import numpy as np
#import pandas as pd
from baseMF import baseMF
#import matplotlib.pyplot as plt
#from remtime import *
from collections import deque
#from remtime import printTime
import os
import time
import heapq
import math
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = ""

class MSVD(baseMF):
    def __init__(self, core_shape=[10,10,3],criteriaNum = 6, criReg = 0.001,**kwargs):
        super(MSVD, self).__init__(**kwargs)
        self.criteriaNum = criteriaNum + 1
        self.core_shape = core_shape
        reg = kwargs.get('reg', None)
        if reg:
            self.criReg = reg
        else:
            self.criReg = criReg
        self.core = tf.Variable(tf.random_normal([core_shape[0],core_shape[1], core_shape[2]])/np.sqrt(core_shape[0]))
        self.ratingBatch = tf.placeholder(tf.float32, [None,self.criteriaNum], name='ratingBatch')
        self.userWeight = tf.Variable(tf.random_normal([self.users, core_shape[0]])/np.sqrt(self.users))
        self.itemWeight = tf.Variable(tf.random_normal([self.items, core_shape[1]])/np.sqrt(self.items))
        self.ceriteraWeight = tf.Variable(tf.random_normal([self.criteriaNum, core_shape[2]])/np.sqrt(self.criteriaNum))

    def getData(self, train=None, test=None, ignore=False,):
        m = train.max() + 1
        if (not ignore) and (m[0] != self.users):
            self.logger.info(
                'error: the user num [%d] is not equal the maximum user ID [%d] in data,please check or setting ignore=True' % (
                    self.users, m[0]))
            #return
        if (not ignore) and (m[1] != self.items):
            self.logger.info(
                'error: the item num [%d] is not equal the maximum item ID [%d] in data,please check or setting ignore=True' % (
                    self.items, m[1]))
            #return
        self.trainData = train.values[:, :2 + self.criteriaNum ]
        self.testData = test.values[:, :3 ]
        self.trRow = self.trainData.shape[0]
        self.tsRow = self.testData.shape[0]

    def buildGraph(self):
        userWeightBatch = tf.nn.embedding_lookup(self.userWeight, self.userBatch)
        itemWeightBatch = tf.nn.embedding_lookup(self.itemWeight, self.itemBatch)
        reconstruct = tf.tensordot(tf.tensordot(tf.tensordot(self.core,userWeightBatch,[0,1]),itemWeightBatch,[0,1]),self.ceriteraWeight,[0,1])
        bs = tf.range(tf.shape(userWeightBatch)[0])
        predrating = tf.gather_nd(reconstruct,tf.transpose([bs,bs]))
        prediction = tf.gather_nd(reconstruct[:,:,2],tf.transpose([bs,bs]))
        base = tf.nn.l2_loss(tf.subtract(self.ratingBatch, predrating))
        uireg = tf.add(self.uReg *tf.nn.l2_loss(self.userWeight), self.iReg * tf.nn.l2_loss(self.itemWeight))
        reg = tf.add(uireg,self.criReg *tf.nn.l2_loss(self.ceriteraWeight))
        cost = base + reg
        return prediction, cost

    def trainIter(self, pre, cost, optimizer,shuffle):
        errors = deque()
        num_batch_loop = int(self.trRow / self.batchSize)
        if shuffle:
            np.random.shuffle(self.trainData)
        t = time.time()
        for i in range(num_batch_loop):
            _, c, pred_batch = self.sess.run([optimizer, cost, pre],
                                             feed_dict={self.userBatch: self.trainData[
                                                                        i * self.batchSize:(i + 1) * self.batchSize, 0],
                                                        self.itemBatch: self.trainData[
                                                                        i * self.batchSize:(i + 1) * self.batchSize, 1],
                                                        self.ratingBatch: self.trainData[
                                                                          i * self.batchSize:(i + 1) * self.batchSize,
                                                                          2:]})
            pred_batch = np.clip(pred_batch, self.minRating, self.maxRating).reshape(-1)
            errors.append(np.mean(
                np.power(pred_batch - self.trainData[i * self.batchSize:(i + 1) * self.batchSize, 2], 2)))
        if self.trRow % self.batchSize:
            _, c, pred_batch = self.sess.run([optimizer, cost, pre],
                                             feed_dict={self.userBatch: self.trainData[(i + 1) * self.batchSize:, 0],
                                                        self.itemBatch: self.trainData[(i + 1) * self.batchSize:, 1],
                                                        self.ratingBatch: self.trainData[(i + 1) * self.batchSize:,
                                                                          2:]})
            pred_batch = np.clip(pred_batch, self.minRating, self.maxRating).reshape(-1)
            errors.append(np.mean(
                np.power(pred_batch - self.trainData[(i + 1) * self.batchSize:, 2], 2)))
        trRMSE = np.sqrt(np.mean(errors))
        return trRMSE, time.time() - t