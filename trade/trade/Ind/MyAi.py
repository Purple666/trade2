# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 22:46:51 2016

@author: salem7mg
"""
from sklearn import svm, datasets, grid_search, metrics,cross_validation,tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.cross_validation import train_test_split
class MyAi:
    def MyAiTree():
        clf = tree.DecisionTreeClassifier()
        return clf
    def MyAiRandam():
        #clf = RandomForestClassifier(n_estimators=11, random_state=1000)
        clf = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=3, max_features='auto', max_leaf_nodes=None,
            min_samples_leaf=1, min_samples_split=5,
            min_weight_fraction_leaf=0.0, n_estimators=300, n_jobs=3,
            oob_score=False, random_state=0, verbose=0, warm_start=False)
        return clf
    def MyTAiFit(clf,ds,lb):    
        clf.fit(ds, lb) # 学習
        return clf
    def MyTAiDump(clf,nm):
        joblib.dump(clf,nm) 
        return
