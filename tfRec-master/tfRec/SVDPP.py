import tensorflow as tf
import numpy as np
# import pandas as pd
from BMF import  BMF

# from remtime import printTime
class SVDPP(BMF):
    def __init__(self, **kwargs):
        super(SVDPP,self).__init__(**kwargs)
        self.yWeight = tf.Variable(tf.random_normal([self.items, self.K]) / np.sqrt(self.items))

    def getData(self, train=None, test=None, ignore=False):
        super(SVDPP, self).getData(train,test,ignore)
        self.globalBias = self.trainData[2].mean()
        N = tf.SparseTensor(self.trainData[:, :2], values=[1] * self.trRow, dense_shape=[self.users, self.items])
        self.N = tf.sparse_transpose(N)

    def buildGraph(self):
        # userBatch, itemBatch, ratingBatch = it.get_next()
        yu = tf.nn.embedding_lookup_sparse(self.yWeight, self.N, sp_weights=None, combiner='sqrtn')
        userWeightBatch = tf.nn.embedding_lookup(self.userWeight, self.userBatch)
        itemWeightBatch = tf.nn.embedding_lookup(self.itemWeight, self.itemBatch)

        yuWeightBatch =  tf.nn.embedding_lookup(yu, self.itemBatch)

        userBiasBatch = tf.nn.embedding_lookup(self.userBias, self.userBatch)
        itemBiasBatch = tf.nn.embedding_lookup(self.itemBias, self.itemBatch)

        output = tf.reduce_sum(tf.multiply(userWeightBatch, tf.add(itemWeightBatch, yuWeightBatch)), 1)
        output = tf.add(output, self.globalBias)
        output = tf.add(output, userBiasBatch)
        prediction = tf.add(output, itemBiasBatch)

        base = tf.nn.l2_loss(tf.subtract(prediction, self.ratingBatch))
        reg = self.reg * tf.add(tf.add(tf.nn.l2_loss(userWeightBatch), tf.nn.l2_loss(itemWeightBatch)),tf.nn.l2_loss(yuWeightBatch))
        cost = tf.add(base, reg)
        # r = tf.clip_by_value(prediction,self.minRating,self.maxRating)
        # error = tf.reduce_mean(tf.pow(tf.subtract(r, self.ratingBatch),2))
        # print ('OK')
        return prediction, cost  # ,error


# if __name__ == '__main__':

#     dataset = 'yl'
#     cv = 0
#     train = pd.read_csv('datasets/%s.cv%d.base'%(dataset,cv), sep='\t', header=None)
#     test = pd.read_csv('datasets/%s.cv%d.test'%(dataset,cv), sep='\t', header=None)
#     A = SVDPP(items = 7045,users = 920,epochs=100,reg = 0.01,learningRate=0.001,batchSize=128)
#     A.getData(train = train,test = test,ignore=True)
#     A.train()
