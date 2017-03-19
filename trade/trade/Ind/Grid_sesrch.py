# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 01:44:37 2016

@author: salem7mg
"""
from sklearn import svm, datasets, grid_search, metrics,cross_validation,tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.cross_validation import train_test_split

import multiprocessing as mp
import os
import sys
sys.path.append('/home/salem7mg/AzumiSanjin/Ind')
import time
import numpy as np
import talib
import main2
from sklearn.grid_search import GridSearchCV 
from sklearn import datasets
from sklearn.externals import joblib

from MyInd import MyInd

parameters = {
        'n_estimators'      : [5, 10, 20, 30, 50, 100, 300],
        'random_state'      : [0],
        'n_jobs'            : [3],
        'min_samples_split' : [5, 10, 15],
        'max_depth'         : [3, 5, 10, 15, 20, 25, 30, 40, 50, 100]
}
def IndGrid(Sybol,TimeFrame,fromx,to):
    can=np.array(MyInd.CanRead(Sybol,TimeFrame,fromx,to))
    label=main2.IndPredict(can,9,9)
    p = mp.Pool(mp.cpu_count())
    processes = []
    for i in range(len(main2.Ind)):
    #for i in range(1):
        processes.append((main2.TrVal1,Sybol,TimeFrame,i,can[:len(can)],9,9))
    p.map(main2.argwrapper,processes)
    p.close()
    processes = []
    del p
    tmpdir='/tmp/'

    for i in range(len(main2.Ind)):            
        if not os.path.exists('/home/salem7mg/Documents/Python/'+main2.Ind[i][1]+".txt"):            
            features=np.load(tmpdir+Sybol+TimeFrame+main2.Ind[i][1]+'.npy')
            clf = GridSearchCV(RandomForestClassifier(), parameters)
            clf.fit(features, label)
            fo = open('/home/salem7mg/Documents/Python/'+main2.Ind[i][1]+".txt", 'w')
            sys.stdout = fo
            print(main2.Ind[i][1]+"best-->",clf.best_estimator_)
            print("\n+ トレーニングデータでCVした時の平均スコア:\n")
            for params, mean_score, all_scores in clf.grid_scores_:
                print ("{:.3f} (+/- {:.3f}) for {}".format(mean_score, all_scores.std() / 2, params))

                print ("\n+ テストデータでの識別結果:\n")
        #y_true, y_pred = y_test, clf.predict(X_test)
        #print (classification_report(y_true, y_pred))
            """        
        for j in range(i+1,len(main2.Ind)):
            fo = open('/home/salem7mg/Documents/Python/'+main2.Ind[i][1]+main2.Ind[j][1]+"txt", 'w')
            sys.stdout = fo
            main2.TrValx(Sybol,TimeFrame,i,j)
            features=np.load(tmpdir+Sybol+TimeFrame+main2.Ind[i][1]+main2.Ind[j][1]+'.npy') 
            os.remove(tmpdir+Sybol+TimeFrame+main2.Ind[i][1]+main2.Ind[j][1]+'.npy')
            clf = GridSearchCV(RandomForestClassifier(), parameters)
            clf.fit(features, label)
            print(main2.Ind[i][1]+main2.Ind[j][1]+"best-->",clf.best_estimator_)
            print("\n+ トレーニングデータでCVした時の平均スコア:\n")
            for params, mean_score, all_scores in clf.grid_scores_:
                print ("{:.3f} (+/- {:.3f}) for {}".format(mean_score, all_scores.std() / 2, params))

            print ("\n+ テストデータでの識別結果:\n")
            y_true, y_pred = y_test, clf.predict(X_test)
            print (classification_report(y_true, y_pred))
        """
        os.remove(tmpdir+Sybol+TimeFrame+main2.Ind[i][1]+'.npy')
    sys.stdout = sys.__stdout__
    return
        
if __name__ == '__main__':
    #IndMain2('USDJPY','10080','0','1167429600')
    #IndMain2('USDJPY','1440','0','1167429600')
    #IndMain2('USDJPY','240','0','1167429600')
    #IndMain2('USDJPY','60','0','1167429600')
    #IndGrid('USDJPY','30','0','1167429600')
    IndGrid('USDJPY','15','0','1167429600')
    #IndMain2('USDJPY','5','0','1167429600')
    #IndMain2('USDJPY','1','0','1167429600')

