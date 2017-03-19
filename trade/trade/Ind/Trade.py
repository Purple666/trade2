import os
import sys
sys.path.append('/home/salem7mg/AzumiSanjin/Ind')
import time
import numpy as np
import talib
import main2
from sklearn import datasets
from sklearn.externals import joblib

from MyInd import MyInd
OP_BUY =0
OP_SELL =1 
OP_BUYLIMIT =2 
OP_SELLLIMIT =3
OP_BUYSTOP =4 
OP_SELLSTOP =5
def AiLoad(Dayvalue):
    clf=[]
          
    filedir='/home/salem7mg/Documents/Python/data/'+"USDJPY"+str(que.timeframe[0])+"/"
    #filedir='/home/salem7mg/Documents/Python/data/'+"USDJPY"+'15'+"/"
    for j  in range(1):
        #for j  in range(len(main2.Ind)-1):
        """                
        clf.append(joblib.load(filedir+que.parename[0][0:6]
            +str(que.timeframe[0])+main2.Ind[j][1]))
            """
            #for k  in range(j+1,10):
        for k  in range(j+1,len(main2.Ind)):
            clf.append(joblib.load(filedir+que.parename[0][0:6]+str(que.timeframe[0])+main2.Ind[j][1]+main2.Ind[k][1]))
            #clf.append(joblib.load(filedir+que.parename[0][0:6]+'15'+main2.Ind[j][1]+main2.Ind[k][1]))
    return clf
i=0

while i < 100:
    que=MyInd.QueRead()
    if len(que) !=0 and que.val1[0]>0:
        if i==0:   
            i=1
        idno=que.id
        print("obs=",str(int(que.val1[0])))        
        can=np.array(MyInd.CanRead(que.parename[0][0:6],Timeframe=str(que.timeframe[0]),From=str(int(que.val1[0])),limit="1000"))
        l=-1     
        pre1=[]
        processes = []
        for j  in range(len(main2.Ind)):
        #for j  in range(10):
            processes.append((main2.TrVal1,que.parename[0][0:6],str(que.timeframe[0]),j,can,52,3))        
        p = main2.mp.Pool(main2.mp.cpu_count())
        p.map(main2.argwrapper,processes)
        p.close()
        processes = []
        for j  in range(1):
        #for j  in range(len(main2.Ind)-1):
            #aiarg=[]
            #aiarg.append(j)
            #trvalx=main2.IndAi(que.parename[0][0:6],str(que.timeframe[0]),aiarg)
            #l=l+1
            #print(trvalx[-1])
            #pre1.append(clf[l].predict(trvalx[-1]))
            #for k  in [4]:

            #for k  in range(j+1,10):
            for k  in range(j+1,len(main2.Ind)):
                aiarg=[]
                aiarg.append(j)
                aiarg.append(k)
                processes.append((main2.TrValx,que.parename[0][0:6],str(que.timeframe[0]),j,k))
        p = main2.mp.Pool(main2.mp.cpu_count())
        trvalx = p.map(main2.argwrapper,processes)
        p.close()
        processes = []
        pre1=[]
        for j  in range(1):
            """
            l=l+1
            aiarg=[]
            aiarg.append(j)
            pre1.append(main2.IndAiPredict(clf[l],que.parename[0][0:6],str(que.timeframe[0]),aiarg))
            """
            #for k  in range(j+1,10):
            for k  in range(j+1,len(main2.Ind)):
                l=l+1
                aiarg=[]
                aiarg.append(j)
                aiarg.append(k)
                #main2.IndAiPredict(clf[l],que.parename[0][0:6],str(que.timeframe[0]),aiarg)
                pre1.append(main2.IndAiPredict(clf[l],que.parename[0][0:6],str(que.timeframe[0]),aiarg))
                #processes.append((main2.IndAiPredict,clf[l],que.parename[0][0:6],str(que.timeframe[0]),aiarg))
        #p = main2.mp.Pool(main2.mp.cpu_count())
        #per1 = p.map(main2.argwrapper,processes)
        #p.close()
        """
            for k  in range(j+1,10):
                l=l+1
                pre1.append(clf[l].predict(trvalx[k][-1]))
        """    
        #can=np.array(MyInd.CanRead(que.parename[0][0:6],Timeframe='60',From=str(int(que.val1[0])),limit="200"))
        """        
        pre2=[]
        for j  in range(len(main2.Ind)):
            main2.TrVal1(que.parename[0][0:6],'60',j,can,52,0)        
        for j  in range(3,4):
        #for j  in range(len(main2.Ind)-1):
            aiarg=[]
            aiarg.append(j)
            trvalx=main2.IndAi(que.parename[0][0:6],'60',aiarg)
            l=l+1            
            pre2.append(clf[l].predict(trvalx[0]))
            for k  in range(j+1,len(main2.Ind)-1):
                aiarg=[]
                aiarg.append(j)
                aiarg.append(k)
                main2.TrValx(que.parename[0][0:6],'60',j,k)
                trvalx=main2.IndAi(que.parename[0][0:6],'60',aiarg)
                l=l+1
                pre2.append(clf[l].predict(trvalx[0])[0])
        """
        que.msg[0]=""
        que.op[0]=9
        que.val1[0]=0
        pre1=np.reshape(pre1,-1)
        print (pre1)
        
        if len(pre1[pre1>0]) > 0 and len(pre1[pre1<0])<len(pre1[pre1>0]): 
            pre0=int(sum(pre1[pre1>0]) / len(pre1[pre1>0])) 
        elif len(pre1[pre1<0]) >0 and len(pre1[pre1>0])<len(pre1[pre1<0])-2: 
            pre0=int(sum(pre1[pre1<0]) / len(pre1[pre1<0])) 
        else:
            pre0=0
        #pre0=np.median(np.array(np.where(pre1!=0)),axis=0)
        #pre0=np.sum(np.array(pre1))/(l+1)
        """
        if pre0<=1 and pre0>=-1:
            pre0=np.median(np.array(pre2),axis=0)*4
        """
        print("pre0=",pre0)
        if pre0 !=0: 
            que.msg[0]="order"
            if pre0>= 1 :
                que.op[0]=0
                que.val1[0]= pre0
                pre= pre0
            elif pre0 <= -1 :
                que.op[0]=1
                que.val1[0]= pre0
                pre= pre0*-1
            else:
                que.op[0]=9
        else:
            que.op[0]=9
                     
        MyInd.QueIns(que)
        MyInd.QueUpdt(que.id)
    time.sleep(0.1)

if __name__ == '__main__':
    que=MyInd.QueRead()
    if len(que) !=0 and que.val1[0]>0:
        idno=que.id
        print("obs=",str(int(que.val1[0])))        
        que.msg[0]="trfit"
            
