# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 08:34:20 2016

@author: salem7mg
"""
import numpy as np
import multiprocessing as mp
import itertools as itrt
import main2 as ma

class MyMultiProcess:
    ###def __init__():

    def parallel_calculation(self, core_num, array):
        indx={}
        can=MyInd.CanRead(Symbol='usdjpy',To='1167429600')
        Ind=IndTab()
        filedir='/home/salem7mg/Documents/Python/data/'
        label=IndPredict(can,9)
        np.savez(filedir+'label'+'.npz',tr=np.array(label))
        for i in range(len(Ind)):
            trname=Ind[i][1]
            print([Ind[i][1]])
            trval1=list(IndCalc(Ind[i],can[:len(can)-9]))
            if Ind[i][0] == 0:
                trvalx=IndRatio(trval1)
            else:
                trvalx=list(trval1)
                np.savez(filedir+trname+'.npz',tr=np.array(trvalx))
                for j in range(i+1,len(Ind)):
                    print([Ind[i][1]],[Ind[j][1]])
                    trname2=trname+Ind[j][1]
                    trval2=IndCalc(Ind[j],can[:len(can)-9])
                    if Ind[i][0] == 0 and Ind[j][0] == 0:
                        trvalx=IndRatio(npJoin(trval1,trval2))
                    elif Ind[i][0] == 0 and Ind[j][0] != 0:
                        trvalx=npJoin(IndRatio(trval1),trval2)
                    elif Ind[i][0] !=0 and Ind[j][0] == 0:
                        trvalx=npJoin(trval1,IndRatio(trval2))
                    elif Ind[i][0] !=0  and Ind[j][0] !=0 :
                        trvalx=npJoin(trval1,trval2)
                np.savez(filedir+trname2+'.npz',tr=np.array(trvalx))

    def parallel_calculation(self, core_num, array):
        pool = mp.Pool(core_num)
        args = itrt.izip(itrt.repeat(self), itrt.repeat('calculate'), array)
        result = pool.map(tomap, args)
        return result


def toapply(class_name, method_name, *args, **kwargs):
    return getattr(class_name, method_name)(*args, **kwargs)

def tomap(args):
    return getattr(args[0], args[1])(*args[2:]) 
