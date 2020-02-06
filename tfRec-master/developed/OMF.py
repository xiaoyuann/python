import tensorflow as tf
import numpy as np
import pandas as pd
from baseMF import  baseMF
from regression import regressionModel

class OMF(baseMF):
    def __init__(self,convReg = 0.1,regressionReg=0.001 ,**kwargs):
        #criteriaNum mean the Number of sub-criteria/subrating
        super(OMF, self).__init__(**kwargs)
        #self.userBatch = tf.placeholder(tf.int32, [None,1], name='userBatch')
        #self.itemBatch = tf.placeholder(tf.int32, [None,1], name='itemBatch')
        self.conv =tf.layers.Conv2D(filters=1,kernel_size=(1,self.K),strides = (1,1),kernel_regularizer=tf.keras.regularizers.l2(l=convReg) )
        self.regre = regressionModel(_mod = 'linear',reg=regressionReg)

    def buildGraph(self):
        # userBatch, itemBatch, ratingBatch = it.get_next()
        userWeightBatch = tf.nn.embedding_lookup(self.userWeight, self.userBatch)
        itemWeightBatch = tf.nn.embedding_lookup(self.itemWeight, self.itemBatch)
        userWeightBatch = tf.reshape(userWeightBatch,[-1,1,self.K])
        itemWeightBatch = tf.reshape(itemWeightBatch, [-1,1,self.K])
        relation = tf.matmul(tf.transpose(userWeightBatch, perm=[0, 2, 1]), itemWeightBatch)
        net_input = tf.expand_dims(relation, -1)
        prediction = self.regre(tf.layers.flatten(self.conv(net_input)))
        #prediction = tf.reduce_sum(tf.multiply(userWeightBatch, itemWeightBatch), 1)
        base = tf.nn.l2_loss(tf.subtract(prediction, self.ratingBatch))
        #reg = self.reg * tf.add(tf.nn.l2_loss(userWeightBatch), tf.nn.l2_loss(itemWeightBatch))
        reg =  tf.add(self.uReg *tf.nn.l2_loss(self.userWeight), self.iReg * tf.nn.l2_loss(self.itemWeight))
        cost = tf.add(base, reg) +tf.losses.get_regularization_loss()
        # r = tf.clip_by_value(prediction,self.minRating,self.maxRating)
        # error = tf.reduce_mean(tf.pow(tf.subtract(r, self.ratingBatch),2))
        # print ('OK')
        return prediction, cost

if __name__ == '__main__':
    dataset = 'ta'
    cv = 0
    train = pd.read_csv('datasets/%s.cv%d.base' % (dataset, cv), sep='\t', header=None)
    test = pd.read_csv('datasets/%s.cv%d.test' % (dataset, cv), sep='\t', header=None)
    # A = baseMF(items = 7045,users = 920,epochs=1400,reg =  0.1,learningRate=0.001)
    A = OMF(items=5566, users=1742, epochs=500, iReg=0.001, uReg=0.00, learningRate=0.01, batchSize=32,
               optimizer='sgd',log = 'logs/OMF')
    A.getData(train=train, test=test)
    A.train()
    print(A.testPrediction)