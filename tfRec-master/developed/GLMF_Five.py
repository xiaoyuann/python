import  tensorflow as tf


from GLMF import GLMF
import pandas as pd
import numpy as np
import os
import sys
import time 
import logging


if __name__ == '__main__':
    '''
    Example: $ pypy runner_hes_pypy.py mt 2 30 0 5.0 1.0
    '''
    if len(sys.argv) < 3:
        #folder_name = 'epinions'
        dataset = 'ta'
        _K =5
        Rnd = 3
        #pc = 7 # 70% training.
        cv = 10
        percent = '02'# cv index
        maxR = 5.0
        minR = 1.0
        criteriaNum =6
        lr= 0.001
        biasR = 0.08
        uR = 0.01
        iR = 0.01
        regressionR = 0.1
        lam = 0.1
    elif len(sys.argv) < 16:
        dataset = sys.argv[1]
        _K = int(sys.argv[2])
        Rnd = int(sys.argv[3])
        #pc = int(sys.argv[4])
        cv = int(sys.argv[4])
        percent = sys.argv[5]# cv index
        maxR = float(sys.argv[6])
        minR = float(sys.argv[7])
        criteriaNum = int(sys.argv[8])
        lr= float(sys.argv[9])
        biasR = float(sys.argv[10])
        uR = float(sys.argv[11])
        iR =float(sys.argv[12])
        regressionR =float(sys.argv[13])
        lam = float(sys.argv[14])
    else:
        dataset = sys.argv[1]
        _K = int(sys.argv[2])
        Rnd = int(sys.argv[3])
        #pc = int(sys.argv[4])
        cv = int(sys.argv[4])
        percent = sys.argv[5]# cv index
        maxR = float(sys.argv[6])
        minR = float(sys.argv[7])
        criteriaNum = int(sys.argv[8])
        lr= float(sys.argv[9])
        biasR = float(sys.argv[10])
        uR = float(sys.argv[11])
        iR =float(sys.argv[12])
        regressionR =float(sys.argv[13])
        lam = float(sys.argv[14])
        GPU = sys.argv[15]
        os.environ['CUDA_VISIBLE_DEVICES']= GPU
        

    train = pd.read_csv('../datasets/%s.cv%d.%s.base'%(dataset,cv,percent), sep='\t', header=None)
    test = pd.read_csv('../datasets/%s.cv%d.%s.test'%(dataset,cv,percent), sep='\t', header=None)
    items_num = train[1].max()+1
    user_num = train[0].max()+1
    sStr = '%s_K%d_cv%d_percent%s'%(dataset,_K,cv,percent)
    logroot = 'logs/'
    logName = r'%s%s_%s.log'%(logroot,sStr,time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime()))#logroot +sStr + '_' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  +".log"
    #fh = logging.FileHandler(logName, mode='w')
    print('log save as: %s'%(logName))
    #log_file = open(logName, "w")
    #sys.stdout = log_file
    #print(sStr)
    A = GLMF(K=_K,items = items_num,users = user_num,epochs=Rnd,regressionReg=regressionR, iReg=iR, criteriaNum = criteriaNum, uReg = uR, biasReg =biasR,learningRate=lr,lambd = lam,alpha=0.5,batchSize=1,saveStr = sStr,log = logName, optimizer='rmsprop')
    A.getData(train = train,test = test)
    #A.train(mod='auto')
    A.train(mod='cpu',cpu_cores=1)
    #print (np.abs(A.testPrediction-test[2]).mean())
    #print('RMSE:')
    print('RMSE:')
    bestRMSE = np.sqrt(np.power(A.testPrediction - test[2], 2).mean())
    print(bestRMSE)
    print('MAE:')
    print(np.abs(A.testPrediction - test[2]).mean())
    pd.DataFrame(A.testPrediction).to_csv('result/%s_%s_K%d_cv%s_RMSE%s_lambd%s.csv' % (A.__class__.__name__,dataset,_K, cv,round(bestRMSE, 4), A.lambd),
                                          header=None, index=None)
    print('---------------------------Finish--------------------------------------')
    #log_file.close()
    #sys.stdout = stdout_backup