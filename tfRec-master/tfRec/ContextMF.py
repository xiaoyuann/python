__author__ = 'FanGhost'
__date__ = '1/30/2018'

import tensorflow as tf
import numpy as np
#import pandas as pd
from BMF import  BMF
import time
from collections import deque
from regression import regressionModel

class CIC(BMF):
    def __init__(self,mod = 'Linear',criteriaNum = 3,lambd = 0.01,alpha = 0.01,regressionReg=0.01, **kwargs):
        #criteriaNum mean the Number of sub-criteria/subrating
        super(CIC, self).__init__(**kwargs)
        #self.ratingBatch = tf.placeholder(tf.float32, [None], name='ratingBatch')
        self.criteriaNum = criteriaNum
        self.lambd = lambd
        self.alpha = alpha
        self.subRatingBatch = tf.placeholder(tf.float32, [None,criteriaNum], name='subRatingBatch')
        self.regression = regressionModel(_mod = mod,reg=regressionReg)


    def getData(self, train=None, test=None, ignore=False,):
        m = train.max() + 1
        if (not ignore) and (m[0] != self.users):
            #print(
            self.logger.info(
                'error: the user num [%d] is not equal the maximum user ID [%d] in data,please check or setting ignore=True' % (
                    self.users, m[0]))
            #return
        if (not ignore) and (m[1] != self.items):
            self.logger.info(#print(
                'error: the item num [%d] is not equal the maximum item ID [%d] in data,please check or setting ignore=True' % (
                    self.items, m[1]))
            #return
        self.trainData = train.values[:, :3 + self.criteriaNum ]
        self.testData = test.values[:, :3+ self.criteriaNum ]
        self.trRow = self.trainData.shape[0]
        self.tsRow = self.testData.shape[0]

    def buildGraph(self):
        # userBatch, itemBatch, ratingBatch = it.get_next()
        self.globalBias = tf.constant(self.trainData[:,2:3].mean(axis=0),dtype=tf.float32)
        self.globalSubBias = tf.constant(self.trainData[:,3:].mean(axis=0),dtype=tf.float32)
        userWeightBatch = tf.nn.embedding_lookup(self.userWeight, self.userBatch)
        itemWeightBatch = tf.nn.embedding_lookup(self.itemWeight, self.itemBatch)

        userBiasBatch = tf.nn.embedding_lookup(self.userBias, self.userBatch)
        itemBiasBatch = tf.nn.embedding_lookup(self.itemBias, self.itemBatch)

        output = tf.reduce_sum(tf.multiply(userWeightBatch, itemWeightBatch), 1)
        output = tf.add(output, self.globalBias)
        output = tf.add(output, userBiasBatch)
        globalPrediction = tf.add(output, itemBiasBatch)

        prediction = (1-self.alpha)*globalPrediction +  self.alpha * tf.reshape(self.regression(self.subRatingBatch),[-1])
        base = tf.nn.l2_loss(tf.subtract(prediction, self.ratingBatch))

        globalReg = tf.add(self.uReg *tf.nn.l2_loss(userWeightBatch), self.iReg * tf.nn.l2_loss(itemWeightBatch))
        bReg = tf.add(tf.nn.l2_loss(userBiasBatch), tf.nn.l2_loss(itemBiasBatch))
        #bReg = tf.add(bReg, tf.nn.l2_loss(globalBias))
        reg = tf.add(globalReg, self.biasReg *bReg)

        globalCost = tf.add(base, reg)

        # print ('OK')
        return prediction, globalCost
    
    def trainIter(self, pre, cost, optimizer,shuffle):
        num_batch_loop = int(self.trRow / self.batchSize)
        if shuffle:
            np.random.shuffle(self.trainData)
        prediction = []
        errors = deque()
        t = time.time()
        for i in range(num_batch_loop):
            _, c, pred_batch = self.sess.run([optimizer, cost, pre],
                                        feed_dict={self.userBatch: self.trainData[i * self.batchSize:(i + 1) * self.batchSize,0],
                                                    self.itemBatch: self.trainData[i * self.batchSize:(i + 1) * self.batchSize,1],
                                                    self.ratingBatch: self.trainData[i * self.batchSize:(i + 1) * self.batchSize,2:3],
                                                    self.subRatingBatch: self.trainData[i * self.batchSize:(i + 1) * self.batchSize,3:]})
            pred_batch = np.clip(pred_batch, self.minRating, self.maxRating).reshape(-1)

            # print type(pred_batch)
            errors.append(np.mean(
                np.power(pred_batch - self.trainData[i * self.batchSize:(i + 1) * self.batchSize, 2], 2)))
        if self.trRow % self.batchSize:
            _, c, pred_batch = self.sess.run([optimizer, cost, pre],
                                                feed_dict={self.userBatch: self.trainData[(i + 1) * self.batchSize:, 0],
                                                        self.itemBatch: self.trainData[(i + 1) * self.batchSize:, 1],
                                                        self.ratingBatch: self.trainData[(i + 1) * self.batchSize:,2:3],
                                                        self.subRatingBatch: self.trainData[(i + 1) * self.batchSize:,3:]})
            pred_batch = np.clip(pred_batch, self.minRating, self.maxRating).reshape(-1)
            # print type(pred_batch)
            errors.append(np.mean(
                np.power(pred_batch - self.trainData[(i + 1) * self.batchSize:, 2], 2)))
        trRMSE = np.sqrt(np.mean(errors))
        return trRMSE, time.time() - t

    def testIter(self,pre):
        num_batch_loop = int(self.tsRow / self.tsbatchSize)
        prediction = []
        #errors = deque()
        t1 = time.time()
        for i in range(num_batch_loop):
            pred_batch = pre.eval(
                {self.userBatch: self.testData[i * self.tsbatchSize:(i + 1) * self.tsbatchSize, 0],
                 self.itemBatch: self.testData[i * self.tsbatchSize:(i + 1) * self.tsbatchSize, 1],
                self.subRatingBatch: self.testData[i * self.tsbatchSize:(i + 1) * self.tsbatchSize, 3:]},session=self.sess)
            pred_batch = np.clip(pred_batch, self.minRating, self.maxRating).reshape(-1)
            prediction.append(pred_batch)
            
        if (self.tsRow % self.tsbatchSize):
            pred_batch = pre.eval(
                {self.userBatch: self.testData[(i + 1) * self.tsbatchSize:, 0],
                 self.itemBatch: self.testData[(i + 1) * self.tsbatchSize:, 1],
                self.subRatingBatch: self.testData[(i + 1) * self.tsbatchSize:, 3:]}, session=self.sess)
            pred_batch = np.clip(pred_batch, self.minRating, self.maxRating).reshape(-1)
            prediction.append(pred_batch)

        # TS_epoch_loss = np.sqrt(np.mean(errors))
        # RMSEts.append(TS_epoch_loss)

        # self.testPrediction = np.concatenate(prediction)
        tsRMSE = np.sqrt(np.power(np.concatenate(prediction) - self.testData[:, 2], 2).mean())
        tsMAE = np.abs(np.concatenate(prediction) - self.testData[:, 2]).mean()
        return tsMAE,tsRMSE,time.time() - t1,prediction
    
#class CCC(BMF):
    


# if __name__ == '__main__':
#     dataset = 'br'
#     cv = 0
#     train = pd.read_csv('datasets/%s.cv%d.base'%(dataset,cv), sep='\t', header=None)
#     test = pd.read_csv('datasets/%s.cv%d.test'%(dataset,cv), sep='\t', header=None)
#     #A = GLMF(items = 7045,users = 920,epochs=100,reg = 0.1 ,learningRate=0.001,lambd = 0.1,alpha=0.1,batchSize=128,mod='Mean')
#     A = CIC(items=48923, users=10574, epochs=1500, reg=0.1, learningRate=0.0005, batchSize=128,lambd = 0.1,alpha=1,criteriaNum=5)
#     A.getData(train = train,test = test)
#     A.train()
