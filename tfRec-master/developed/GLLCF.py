__author__ = 'FanGhost'
__date__ = '3/19/2018'
# from hes_pypy import  load_data#, #MF

import time
import pickle
import sys
import logging
# import pandas as pd
import random
import time
from math import sqrt
from math import log as Log
from math import e as E
import logging
import pickle

xrange =range
def count(li):
    c0, c1, c2 = 0, 0, 0
    for l in li:
        if l == 0:
            c0 += 1
        elif l == 1:
            c1 += 1
        else:
            c2 += 1
    return [c0, c1, c2]


def root_mean_squared_error(predictions, targets):
    tmp = [(predictions[i] - targets[i]) ** 2 for i in xrange(len(predictions))]
    return sqrt(mean(tmp))


def mean_absolute_error(predictions, targets):
    tmp = [abs(predictions[i] - targets[i]) for i in xrange(len(predictions))]
    return mean(tmp)


def inner(A, B):
    return sum([A[i] * B[i] for i in xrange(len(A))])


def product(A, n):
    return [A[i] * n for i in xrange(len(A))]


def sum1(A, B):
    return [A[i] + B[i] for i in xrange(len(A))]


def sum0(A, n):
    return [A[i] + n for i in xrange(len(A))]


def mean(L):
    return sum(L) / float(len(L))


def argmin(L):
    min_idx, min_v = 0, L[0]
    for i, l in enumerate(L):
        if l < min_v:
            min_idx = i
            min_v = l
    return min_idx


def argmax(L):
    max_idx, max_v = 0, L[0]
    for i, l in enumerate(L):
        if l > max_v:
            max_idx = i
            max_v = l
    return max_idx


def normailize21(L):
    s = float(sum(L))
    return [l / s for l in L]


def normailize_1(L):
    s = float(sum(L))
    L = [1 - l / s for l in L]
    return normailize21(L)
def load_data(dfile):
    data = []
    user, item = set(),set()
    with open(dfile, 'rb') as f:
        for eline in f:
            li = eline.split()
            user.add(int(li[0]))
            item.add(int(li[1]))
            mainR = float(li[2])
            subR = [float(r) for r in li[3:]]
            data.append([int(li[0]), int(li[1]),mainR, subR])
    return data, (max(user)+1, max(item)+1)

class GLMF():
    def __init__(self, base, n_user, n_item, n_feature, max_rate=5, min_rate=1, criteria_num=3, lambd=0.1):
        """
        base/test: [[uid,iid,rate],...] ndarray or list of int or float
        uid, iid start from 0
        """
        self.n_event = 1.
        self.n_user = n_user
        self.n_item = n_item
        self.n_feature = n_feature
        self.shape = (n_user, n_item)
        self.max_r = max_rate
        self.min_r = min_rate
        self.criteria_num = criteria_num
        self.lambd = lambd

        self.w = [random.gauss(0, 0.01) for i in xrange(criteria_num)]
        y = [e[2] for e in base]
        self.mui = mean(y)  # init as ovwerall mean, will be updated
        reg = 1#float(sqrt(self.n_feature))
        self.b = random.gauss(0, 0.1)
        self.bias_user = product([random.gauss(0, 0.1) for i in xrange(n_user)], 1. / reg)
        self.bias_item = product([random.gauss(0, 0.1) for i in xrange(n_item)], 1. / reg)
        self.factor_user = [product([random.gauss(0, 0.1) for i in xrange(n_feature)], 1. / reg) for j in
                            xrange(n_user)]
        self.factor_item = [product([random.gauss(0, 0.1) for i in xrange(n_feature)], 1. / reg) for j in
                            xrange(n_item)]

        # init sub weights
        sub_y = [[e[3][i] for e in base] for i in xrange(criteria_num)]
        self.sub_mui = [mean(sub_y[i]) for i in xrange(criteria_num)]
        self.sub_bias_user = [product([random.gauss(0, 0.1) for i in xrange(n_user)], 1. / reg) for i in
                              xrange(criteria_num)]
        self.sub_bias_item = [product([random.gauss(0, 0.1) for i in xrange(n_item)], 1. / reg) for i in
                              xrange(criteria_num)]
        self.sub_factor_user = [
            [product([random.gauss(0, 0.1) for i in xrange(n_feature)], 1. / reg) for j in xrange(n_user)] for i in
            xrange(criteria_num)]
        self.sub_factor_item = [
            [product([random.gauss(0, 0.1) for i in xrange(n_feature)], 1. / reg) for j in xrange(n_item)] for i in
            xrange(criteria_num)]

    def fit(self, base, test=None, log='Noname.log', iter_round=20, learn_rate=0.01, bias_reg_u=0.01, bias_reg_i=0.01,
            reg_i=0.01, reg_u=0.01, decay=1., reg_w=0.01, reg_b=0.):
        #def updateLR(self):

        logger = logging.getLogger('mflogger')
        logger.setLevel(logging.DEBUG)
        #
        fh = logging.FileHandler(log)
        fh.setLevel(logging.DEBUG)
        #
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        #
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        #
        logger.addHandler(fh)
        logger.addHandler(ch)

        self.learn_rate = learn_rate
        self.reg_u = reg_u
        self.reg_i = reg_i
        self.bias_reg_u = bias_reg_u
        self.bias_reg_i = bias_reg_i
        self.reg_w = reg_w
        self.reg_b = reg_b
        self.decay = decay
        eps = 1e-8
        beta1 = 0.9
        beta2 = 0.999
        t=0
        reg = float(sqrt(self.n_feature))
        mw = [0 for i in xrange(self.criteria_num)]
        mb = 0
        mbias_user = product([0 for i in xrange(self.n_user)], 1. / reg)
        mbias_item = product([0 for i in xrange(self.n_item)], 1. / reg)
        mfactor_user = [product([0 for i in xrange(self.n_feature)], 1. / reg) for j in
                        xrange(self.n_user)]
        mfactor_item = [product([0 for i in xrange(self.n_feature)], 1. / reg) for j in
                        xrange(self.n_item)]

        # init sub weights

        msub_bias_user = [product([0 for i in xrange(self.n_user)], 1. / reg) for i in
                          xrange(self.criteria_num)]
        msub_bias_item = [product([0 for i in xrange(self.n_item)], 1. / reg) for i in
                          xrange(self.criteria_num)]
        msub_factor_user = [
            [product([0 for i in xrange(self.n_feature)], 1. / reg) for j in xrange(self.n_user)] for i in
            xrange(self.criteria_num)]
        msub_factor_item = [
            [product([0 for i in xrange(self.n_feature)], 1. / reg) for j in xrange(self.n_item)] for i in
            xrange(self.criteria_num)]

        vw = [0 for i in xrange(self.criteria_num)]
        vb = 0
        vbias_user = product([0 for i in xrange(self.n_user)], 1. / reg)
        vbias_item = product([0 for i in xrange(self.n_item)], 1. / reg)
        vfactor_user = [product([0 for i in xrange(self.n_feature)], 1. / reg) for j in
                        xrange(self.n_user)]
        vfactor_item = [product([0 for i in xrange(self.n_feature)], 1. / reg) for j in
                        xrange(self.n_item)]

        # init sub weights

        vsub_bias_user = [product([0 for i in xrange(self.n_user)], 1. / reg) for i in
                          xrange(self.criteria_num)]
        vsub_bias_item = [product([0 for i in xrange(self.n_item)], 1. / reg) for i in
                          xrange(self.criteria_num)]
        vsub_factor_user = [
            [product([0 for i in xrange(self.n_feature)], 1. / reg) for j in xrange(self.n_user)] for i in
            xrange(self.criteria_num)]
        vsub_factor_item = [
            [product([0 for i in xrange(self.n_feature)], 1. / reg) for j in xrange(self.n_item)] for i in
            xrange(self.criteria_num)]
        # update parameters
        gstart = time.clock()
        tttt = time.time()
        for ir in xrange(iter_round):
            t += 1
            learn_rate = self.learn_rate * (1 - beta2 ** t) ** 0.5 / (1 - beta1 ** t)
            y_pred = []
            y = []
            #t =ir+1

            #print(self.learn_rate)
            #
            random.shuffle(base)
            #if ir !=0:
                #print(self.learn_rate * (1 - beta2 ** t) ** 0.5 / (1 - beta1 ** t))
            for [uid, iid, r, subR] in base:
                uid, iid = int(uid), int(iid)
                r_pred = self.predict(uid, iid)
                y.append(r)
                #y_pred.append(r_pred)
                if r_pred > self.max_r:
                    y_pred.append(self.max_r)#r_pred = self.max_r  # mt rates (0,]], rb (0,6]
                elif r_pred < self.min_r:
                    y_pred.append(self.min_r)#r_pred = self.min_r
                else:
                    y_pred.append(r_pred)#r_pred = r_pred

                err = r - r_pred


                # using adam
                #
                '''

                dx = -(err - self.bias_reg_u * self.bias_user[uid])
                mbias_user[uid] = beta1 * mbias_user[uid] + (1 - beta1) * dx
                vbias_user[uid] = beta2 * vbias_user[uid] + (1 - beta2) * (dx ** 2)
                for i in xrange(self.n_user):
                    mt = mbias_user[i]  # / (1 - beta1 ** t)
                    vt = vbias_user[i]  # / (1 - beta2 ** t)
                    # print(m / ((v ** 0.5) + eps))
                    # print(mt / ((vt ** 0.5) + eps))
                    self.bias_user[i] += -learn_rate * mt / ((vt ** 0.5) + eps)
                #mt = mbias_user[uid]  # / (1 - beta1 ** t)
                #vt = vbias_user[uid] #/ (1 - beta2 ** t)
                #print(m / ((v ** 0.5) + eps))
                #print(mt / ((vt ** 0.5) + eps))
                #self.bias_user[uid] += -learn_rate * mt / ((vt**0.5) + eps)

                dx = -(err - self.bias_reg_i * self.bias_item[iid])
                mbias_item[iid] = beta1 * mbias_item[iid] + (1 - beta1) * dx
                vbias_item[iid] = beta2 * vbias_item[iid] + (1 - beta2) * (dx ** 2)
                for i in xrange(self.n_item):
                    mt = mbias_item[i]  # / (1 - beta1 ** t)
                    vt = vbias_item[i]  # / (1 - beta2 ** t)
                    self.bias_item[i] += -learn_rate * mt / ((vt ** 0.5) + eps)
                #mt = mbias_item[iid] #/ (1 - beta1 ** t)
                #vt = vbias_item[iid] #/ (1 - beta2 ** t)
                #self.bias_item[iid] += -learn_rate * mt / ((vt**0.5) + eps)
                for k in xrange(self.n_feature):

                    dx = -(err * self.factor_item[iid][k] -
                                self.reg_u * self.factor_user[uid][k])
                    mfactor_user[uid][k] = beta1 * mfactor_user[uid][k] + (1 - beta1) * dx
                    vfactor_user[uid][k] = beta2 * vfactor_user[uid][k] + (1 - beta2) * (dx ** 2)
                    for i in xrange(self.n_user):
                        mt = mfactor_user[i][k]  # / (1 - beta1 ** t)
                        vt = vfactor_user[i][k]  # / (1 - beta2 ** t)
                        self.factor_user[i][k] += -learn_rate * mt / ((vt ** 0.5) + eps)
                    #mt = mfactor_user[uid][k] #/ (1 - beta1 ** t)
                    #vt = vfactor_user[uid][k] #/ (1 - beta2 ** t)
                    #self.factor_user[uid][k] += -learn_rate * mt / ((vt**0.5) + eps)

                    dx = -(err * self.factor_user[uid][k] -
                                self.reg_i * self.factor_item[iid][k])
                    mfactor_item[iid][k] = beta1 * mfactor_item[iid][k] + (1 - beta1) * dx
                    vfactor_item[iid][k] = beta2 * vfactor_item[iid][k] + (1 - beta2) * (dx ** 2)
                    for i in xrange(self.n_item):
                        mt = mfactor_item[i][k]  # / (1 - beta1 ** t)
                        vt = vfactor_item[i][k]  # / (1 - beta2 ** t)
                        self.factor_item[i][k] += -learn_rate * mt / ((vt ** 0.5) + eps)
                    #mt = mfactor_item[iid][k] #/ (1 - beta1 ** t)
                    #vt = vfactor_item[iid][k] #/ (1 - beta2 ** t)
                    #self.factor_item[iid][k] += -learn_rate * mt / ((vt**0.5) + eps)

                for num in xrange(self.criteria_num):
                    sub_err = subR[num] - self.sub_predict(uid, iid, num)

                    dx = -(self.w[num] * err - self.bias_reg_u * self.sub_bias_user[num][uid] + self.lambd * sub_err)
                    msub_bias_user[num][uid] = beta1 * msub_bias_user[num][uid] + (1 - beta1) * dx
                    vsub_bias_user[num][uid] = beta2 * vsub_bias_user[num][uid] + (1 - beta2) * (dx ** 2)
                    for i in xrange(self.n_user):
                        mt = msub_bias_user[num][i]# / (1 - beta1 ** t)
                        vt = vsub_bias_user[num][i]# / (1 - beta2 ** t)
                        self.sub_bias_user[num][i] += -learn_rate * mt / ((vt**0.5) + eps)
                    #mt = msub_bias_user[num][uid]  # / (1 - beta1 ** t)
                    #vt = vsub_bias_user[num][uid]  # / (1 - beta2 ** t)
                    #self.sub_bias_user[num][uid] += -learn_rate * mt / ((vt ** 0.5) + eps)

                    dx = -(self.w[num] * err - self.bias_reg_i * self.sub_bias_item[num][iid] + self.lambd * sub_err)
                    msub_bias_item[num][iid] = beta1 * msub_bias_item[num][iid] + (1 - beta1) * dx
                    vsub_bias_item[num][iid] = beta2 * vsub_bias_item[num][iid] + (1 - beta2) * (dx ** 2)
                    for i in xrange(self.n_item):
                        mt = msub_bias_item[num][i]  # / (1 - beta1 ** t)
                        vt = vsub_bias_item[num][i]  # / (1 - beta2 ** t)
                        self.sub_bias_item[num][i] += -learn_rate * mt / ((vt ** 0.5) + eps)
                    #mt = msub_bias_item[num][iid] #/ (1 - beta1 ** t)
                    #vt = vsub_bias_item[num][iid]# / (1 - beta2 ** t)
                    #self.sub_bias_item[num][iid]  += -learn_rate * mt / ((vt**0.5) + eps)

                    for k in xrange(self.n_feature):
                        dx = -(self.w[num] * err * self.sub_factor_item[num][iid][k] - self.reg_u *
                                self.sub_factor_user[num][uid][k] + self.lambd * sub_err *
                                self.sub_factor_item[num][iid][k])
                        msub_factor_user[num][uid][k] = beta1 * msub_factor_user[num][uid][k] + (1 - beta1) * dx
                        vsub_factor_user[num][uid][k] = beta2 * vsub_factor_user[num][uid][k] + (1 - beta2) * (dx ** 2)
                        for i in xrange(self.n_user):
                            mt = msub_factor_user[num][i][k]  # / (1 - beta1 ** t)
                            vt = vsub_factor_user[num][i][k]  # / (1 - beta2 ** t)
                            self.sub_factor_user[num][i][k] += -learn_rate * mt / ((vt ** 0.5) + eps)
                        #mt = msub_factor_user[num][uid][k]# / (1 - beta1 ** t)
                        #vt = vsub_factor_user[num][uid][k]# / (1 - beta2 ** t)
                        #self.sub_factor_user[num][uid][k] += -learn_rate * mt / ((vt**0.5) + eps)

                        dx = -(self.w[num] * err * self.sub_factor_user[num][uid][k] - self.reg_i *
                                self.sub_factor_item[num][iid][k] + self.lambd * sub_err *
                                self.sub_factor_user[num][uid][k])
                        msub_factor_item[num][iid][k] = beta1 * msub_factor_item[num][iid][k] + (1 - beta1) * dx
                        vsub_factor_item[num][iid][k] = beta2 * vsub_factor_item[num][iid][k] + (1 - beta2) * (dx ** 2)
                        for i in xrange(self.n_item):
                            mt = msub_factor_item[num][i][k]  # / (1 - beta1 ** t)
                            vt = vsub_factor_item[num][i][k]  # / (1 - beta2 ** t)
                            self.sub_factor_item[num][i][k] += -learn_rate * mt / ((vt ** 0.5) + eps)
                        #mt = msub_factor_item[num][iid][k]# / (1 - beta1 ** t)
                        #vt = vsub_factor_item[num][iid][k]# / (1 - beta2 ** t)
                        #self.sub_factor_item[num][iid][k] += -learn_rate * mt / ((vt**0.5) + eps)
                    for num in xrange(self.criteria_num):
                        # sub_err = subR[num] - self.sub_predict(uid, iid, num)
                        dx = -(err * self.sub_predict(uid, iid, num) - self.reg_w)
                        mw[num] = beta1 * mw[num] + (1 - beta1) * dx
                        vw[num] = beta2 * vw[num] + (1 - beta2) * (dx ** 2)
                        for i in xrange(self.criteria_num):
                            mt = mw[i]  # / (1 - beta1 ** t)
                            vt = vw[i]  # / (1 - beta2 ** t)
                            self.w[i] += -learn_rate * mt / ((vt ** 0.5) + eps)
                        #mt = mw[num]  # / (1 - beta1 ** t)
                        #vt = vw[num]  # / (1 - beta2 ** t)
                        #self.w[num] += -learn_rate * mt / ((vt ** 0.5) + eps)
                    dx = -err + self.reg_b
                    mb = beta1 * mb + (1 - beta1) * dx
                    vb = beta2 * vb + (1 - beta2) * (dx ** 2)
                    mt = mb  # / (1 - beta1 ** t)
                    vt = vb  # / (1 - beta2 ** t)
                    self.b += -learn_rate * mt / ((vt ** 0.5) + eps)


                '''
                #using sgd
                # update main bias
                self.bias_user[uid] = self.bias_user[uid] + self.learn_rate * (
                            err - self.bias_reg_u * self.bias_user[uid])
                self.bias_item[iid] = self.bias_item[iid] + self.learn_rate * (
                            err - self.bias_reg_i * self.bias_item[iid])

                for k in xrange(self.n_feature):
                    self.factor_user[uid][k] = self.factor_user[uid][k] + self.learn_rate * (
                                err * self.factor_item[iid][k] -
                                self.reg_u * self.factor_user[uid][k])
                    self.factor_item[iid][k] = self.factor_item[iid][k] + self.learn_rate * (
                                err * self.factor_user[uid][k] -
                                self.reg_i * self.factor_item[iid][k])
                    # update sub rating
                for num in xrange(self.criteria_num):
                    sub_err = subR[num] - self.sub_predict(uid, iid, num)
                    self.sub_bias_user[num][uid] = self.sub_bias_user[num][uid] + self.learn_rate * (
                            self.w[num] * err - self.bias_reg_u * self.sub_bias_user[num][uid] + self.lambd * sub_err)

                    self.sub_bias_item[num][iid] = self.sub_bias_item[num][iid] + self.learn_rate * (
                            self.w[num] * err - self.bias_reg_i * self.sub_bias_item[num][iid] + self.lambd * sub_err)
                    for k in xrange(self.n_feature):
                        self.sub_factor_user[num][uid][k] = self.sub_factor_user[num][uid][k] + self.learn_rate * (
                                self.w[num] * err * self.sub_factor_item[num][iid][k] - self.reg_u *
                                self.sub_factor_user[num][uid][k] + self.lambd * sub_err *
                                self.sub_factor_item[num][iid][k])
                        #ccc= self.factor_item[num][iid][k]

                        self.sub_factor_item[num][iid][k] = self.sub_factor_item[num][iid][k] + self.learn_rate * (
                                self.w[num] * err * self.sub_factor_user[num][uid][k] - self.reg_i *
                                self.sub_factor_item[num][iid][k] + self.lambd * sub_err *
                                self.sub_factor_user[num][uid][k])
                        # update regression model
                    self.w[num] = self.w[num] + self.learn_rate * (
                                err * self.sub_predict(uid, iid, num) - self.reg_w)

                self.b = self.b + self.learn_rate * err



            y_pred_ = []
            y_ = []
            for [uid, iid, r,_] in test:
                uid, iid = int(uid), int(iid)
                r_pred = self.predict(uid, iid)
                #print(uid,iid)
                #print(r_pred)
                y_.append(r)
                # 1 to 5
                if r_pred > self.max_r:
                    r_pred = self.max_r  # mt rates (0,]], rb (0,6]
                elif r_pred < self.min_r:
                    r_pred = self.min_r
                else:
                    r_pred = r_pred
                y_pred_.append(r_pred)
            # print "Iter %d:  %s --train MAP: %f\tRMSE: %f\t--test MAP: %f\tRMSE: %f"%(ir, time.asctime(),
            #                            mean_absolute_error(y,y_pred),root_mean_squared_error(y,y_pred),
            #                            mean_absolute_error(y_,y_pred_),root_mean_squared_error(y_,y_pred_))
            logger.info("iter %d: %s --train MAE: %f\tRMSE: %f\t--test MAE: %f\tRMSE: %f --%s" % (ir, time.asctime(),
                                                                                                  mean_absolute_error(y,
                                                                                                                      y_pred),
                                                                                                  root_mean_squared_error(
                                                                                                      y, y_pred),
                                                                                                  mean_absolute_error(
                                                                                                      y_, y_pred_),
                                                                                                  root_mean_squared_error(
                                                                                                      y_, y_pred_),
                                                                                                  time.time() - tttt))


    def sub_predict(self, uid, iid, num):
        #print(uid,iid,num)
        return self.sub_mui[num] + self.sub_bias_user[num][uid] + self.sub_bias_item[num][iid] + inner(
            self.sub_factor_user[num][uid], self.sub_factor_item[num][iid])


    def predict(self, uid, iid):
        uid, iid = int(uid), int(iid)
        subR = 0
        for i in xrange(self.criteria_num):
            R = self.sub_predict(uid, iid, i)
            subR = subR + self.w[i] * R
        mainR = self.mui + self.bias_user[uid] + self.bias_item[iid] + inner(self.factor_user[uid], self.factor_item[iid])
        return mainR + subR + self.b

if __name__=='__main__':
    dataset = 'yl'
    dataset = 'br'
    dataset = 'ta'
    # cv = 100
    cv = 10

    base_file = 'datasets/%s.cv%d.base' % (dataset, cv)
    test_file = 'datasets/%s.cv%d.test' % (dataset, cv)
    results_root = 'results/'
    K = 5
    base, shape = load_data(base_file)
    test, _ = load_data(test_file)
    C = 1
    rrr = 0.1
    log_file = results_root + '%s_%s_MF.log' % (dataset, time.asctime().replace(' ', '_').replace(':', '_'))
    print('setup: C=%d, K=%d\ndataset: %s' % (C, K, base_file))

    print('load data finished!')
    Rnd = 100
    mf = GLMF(base, shape[0], shape[1], K, criteria_num=3)
    mf.fit(base, test, iter_round=Rnd, learn_rate=0.001, bias_reg_u=0.1, bias_reg_i=0.1, reg_i=0.01, reg_u=0.01, decay=1.,
           log=log_file)