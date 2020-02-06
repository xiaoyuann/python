__author__ = 'FanGhost'
__date__ = '6/22/2018'
# sharing user or items's componment in matrix factorization,
import tensorflow as tf
import numpy as np
# import pandas as pd
from GLMF import  GLMF
import time
from collections import deque
from regression import regressionModel

class SCMF(GLMF):
    def __init__(self,shared = 'user', **kwargs):
        # criteriaNum mean the Number of sub-criteria/subrating
        #self.logerConfig(log.replace('.log','_%s.log'%self.__class__.__name__))
        self.__class__.__name__ = self.__class__.__name__ + '_%s'%shared
        super(SCMF, self).__init__(**kwargs)
        # self.userSubWeight = tf.Variable(tf.random_normal([self.users, self.K,self.criteriaNum]) / np.sqrt(self.users))
        # self.itemSubWeight = tf.Variable(tf.random_normal([self.items, self.K,self.criteriaNum]) / np.sqrt(self.items))
        if shared == 'i' or shared =='item':
            self.userSubWeight = tf.Variable(
                tf.random_normal([self.users, self.K, self.criteriaNum], stddev=0.1) / np.sqrt(self.K))
            tmpW =self.itemWeight
            tmpB = self.itemBias
            #tmpW = tf.Variable(tf.random_normal([self.items, self.K],stddev = 0.1) / np.sqrt(self.K))
            
            #tmpB = tf.Variable(tf.zeros([self.items]))
            self.itemSubWeight =tf.reshape(tf.gather(tmpW,list(range(self.items))*self.criteriaNum),[self.items, self.K, self.criteriaNum])
            self.itemSubBias = tf.reshape(tf.gather(tmpB,list(range(self.items))*self.criteriaNum),[self.items, self.criteriaNum])
        
        elif shared == 'u' or shared == 'user':
            self.itemSubWeight = tf.Variable(
                tf.random_normal([self.items, self.K, self.criteriaNum], stddev=0.1) / np.sqrt(self.K))
            tmpW =self.userWeight
            tmpB = self.userBias
            #tmpW =tf.Variable(tf.random_normal([self.users, self.K],stddev = 0.1)/ np.sqrt(self.K) )
            #tmpB = tf.Variable(tf.zeros([self.users]))
            self.userSubWeight = tf.reshape(tf.gather(tmpW,list(range(self.users))*self.criteriaNum),[self.users, self.K, self.criteriaNum])
            self.userSubBias = tf.reshape(tf.gather(tmpB,list(range(self.users))*self.criteriaNum),[self.users, self.criteriaNum])
        # self.globalSubBias = tf.Variable(tf.zeros([self.criteriaNum]))

# if __name__ == '__main__':
#     dataset = 'ta'
#     cv = 0
#     train = pd.read_csv('datasets/%s.cv%d.base' % (dataset, cv), sep='\t', header=None)
#     test = pd.read_csv('datasets/%s.cv%d.test' % (dataset, cv), sep='\t', header=None)
#     A = SCMF(items = 5566,users = 1742,epochs=100,reg = 0.1 ,learningRate=0.001,lambd = 0.1,alpha=0.5,batchSize=128)
#     #A = SCMF(items=48923, users=10574, epochs=1500, reg=0.1, learningRate=0.0005, batchSize=128, lambd=0.1, alpha=1,
#     #         criteriaNum=5)
#     A.getData(train=train, test=test)
#     A.train()
