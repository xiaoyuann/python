import tensorflow as tf
import numpy as np
import time
import logging

class autoEncoder():
    def __init__(self,layers = [256,128], reg = 0.001, beta = 5, learningRate=0.005, batchSize=512, epochs=20, users=6041, items=3953,
                 minRating=1., maxRating=5.,pretainName = None, optimizer = 'adam',tsbatchSize=500,th=.89,saveStr ='',log=None):
        self.reg = reg
        self.learningRate = learningRate
        self.batchSize = batchSize
        self.tsbatchSize = tsbatchSize
        self.epochs = epochs
        self.users = users
        self.items = items
        self.minRating = minRating
        self.maxRating = maxRating