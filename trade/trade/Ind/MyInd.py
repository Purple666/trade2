# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:14:20 2016

@author: salem7mg
"""
import Maria
import talib
import numpy as np
class MyInd:
    def CanRead( Symbol,Timeframe='15',From="",To="",limit=""):
        db = Maria.Maria()
        sql = (
                  "SELECT open,low,high,close,volume FROM fx.t_indcan "
                  " WHERE "
                  " Curpare = '" +Symbol+"'" +
                  " AND indnm = 'can' " +
                  " AND TimeFrame = " + str(Timeframe)  
              )
        if From != "" :
            sql = sql + (" AND Obsnumber>=" + From)       
        if To != "" :
            sql = sql + (" AND Obsnumber<=" + To)       
        sql=sql +" ORDER BY Obsnumber "

        if limit != "" :
            sql = sql + (" LIMIT  " + limit)       
        sql=sql +" ; "
        result = tuple(db.inquire(sql))
        return result
    def CanRead2( Symbol,Timeframe='15',From="",To="",limit=""):
        db = Maria.Maria()
        sql = (
                  "SELECT open,low,high,close,volume FROM fx.t_indcan "
                  " WHERE "
                  " Curpare = '" +Symbol+"'" +
                  " AND indnm = 'can' " +
                  " AND TimeFrame = " + str(Timeframe)  
              )
        if From != "" :
            sql = sql + (" AND Obsnumber>=" + From)       
        if To != "" :
            sql = sql + (" AND Obsnumber<=" + To)       
        sql=sql +" ORDER BY Obsnumber desc "

        if limit != "" :
            sql = sql + (" LIMIT  " + limit)       
        sql=sql +" ; "
        result = tuple(db.inquire(sql))
        return result
    def QueRead():
        db = Maria.Maria()
        sql = (
                  "SELECT * "
                  " FROM fxt.t_queue "
                  " WHERE "
                  " rno = 'mg' " +
                  " AND target = 'azumisanji '" +
                  " AND stats = 9" +
                  " AND statr = 0" +
                  " ORDER BY id;"  
              )
        result = db.inquireDf(sql)
        ##db.query("unlock tables;")        
        return result
        
    def QueUpdt(idno):
        idno=list(idno)        
        db = Maria.Maria()
        sql = (
                  "UPDATE  fxt.t_queue "
                  "SET stats = 0"
                  ",statr = 9"
              )
        if len(idno) == 0:
            sql=sql+";"
        else:    
            sql = sql+" WHERE  "
            for i in range(len(idno)):
                if i ==0 :
                    sql = sql+" id= " + str(idno[i])
                else:
                    sql = sql+" OR  id= " + str(idno[i])
            sql = sql+";"
                    
        db.dml(sql)
        return 
    def QueIns(que):
        db = Maria.Maria()
        sql  =     "INSERT  " \
                  " INTO fxt.t_queue  " \
                  "(rno,send,target,stats,statr,msg,parename,op,lots,sl,tp,comment,magic,ticket ,val1) " \
                  " VALUES('mg','azumisanji'" \
                  ",'"+que.send[0] +"'" \
                  ",9,0" \
                  ",'"+que.msg[0]+"'" \
                  ",'"+que.parename[0] +"'" \
                  ","+str(que.op[0]) + \
                  ",0.01,0,0"  +\
                  ",'test'"\
                  ","+str(que.magic[0])+ \
                  ",0" + \
                  "," + str(que.val1[0]) + \
                  ");"
        print(sql)          
        db.dml(sql)
        ##db.query("unlock tables;")        
        return 
    def QueOrd(que):
        db = Maria.Maria()
        val1=str(int(que.val1[0]))
        sql  =     "INSERT  " \
                  " INTO fxt.t_queue  " \
                  "(rno,msg,parename,op,lots,sl,tp,comment,magic,ticket ) " \
                  " VALUES('mg','azumisanji'" \
                  ",'"+que.send[0] +"'" \
                  " ,9,0" \
                  ",'"+que.parename[0] +"'" \
                  ",'"+que.indnm[0] +"'"  + \
                  ","+str(que.timeframe[0])  +\
                  ","+str(que.val1[0]) + \
                  ");"
        print(sql)          
        db.dml(sql)
        ##db.query("unlock tables;")        
        return 
    def Ptn(ds):
        rt=np.zeros_like(ds)
        i=0
        for d  in ds:
            ma=np.max(d)
            mi=np.min(d)
            if ma==mi:
                rt[i]=0
            else:    
                rt[i]=(d-mi) * 100/(ma-mi)
            i=i+1
        return rt    
    def Ich3(ds):
        i=0
        Ichimoku=np.zeros([len(ds),5])    
        i=0;
        for d in  ds:
            if i>52:
                ma=np.max(ds[i-8:i+1,2])
                mi=np.min(ds[i-8:i+1,1])
                Ichimoku[i,0]=(ma + mi) /2 
                ma=np.max(ds[i-25:i+1,2])
                mi=np.min(ds[i-25:i+1,1])
                Ichimoku[i,1]=(ma + mi)  /2
                Ichimoku[i,2]=ds[i,3] 
                if i>len(ds)-26:
                    Ichimoku[i+26,3]=(Ichimoku[i,0]+Ichimoku[i,1]) /2 
                    ma=np.max(ds[i-51:i+1,2])
                    mi=np.min(ds[i-51:i+1,1])
                    Ichimoku[i+26,4]=(ma + mi)  /2 
            i=i+1
        return Ichimoku    
    def Ich(ds):
        i=0
        Tenkan=np.full_like(ds[:,0],np.nan)    
        Kijun =np.full_like(ds[:,0],np.nan)    
        SenkoA=np.full_like(ds[:,0],np.nan)    
        SenkoB=np.full_like(ds[:,0],np.nan)    
        Chikou=np.full_like(ds[:,0],np.nan)    
        i=0
        for d in  ds:
            if i>=52:
                ma=np.max(ds[i-8:i+1,2])
                mi=np.min(ds[i-8:i+1,1])
                Tenkan[i]=(ma + mi) /2 
                ma=np.max(ds[i-25:i+1,2])
                mi=np.min(ds[i-25:i+1,1])
                Kijun[i]=(ma + mi)  /2
                Chikou[i]=ds[i,3] 
                if i<len(ds)-26:
                    SenkoA[i+26]=(Tenkan[i]+Kijun[i]) /2 
                    ma=np.max(ds[i-51:i+1,2])
                    mi=np.min(ds[i-51:i+1,1])
                    SenkoB[i+26]=(ma + mi)  /2 
            i=i+1
        return Tenkan,Kijun,SenkoA,SenkoB,Chikou    
    def IMA(ds,Period=15):
        print("--------------")
        return talib.MA(ds[:,3],Period)
        
    def IEMA(ds,Period=15):
        return talib.EMA(ds[:,3],Period)

    def ISMA(ds,Period=15):
        return talib.SMA(ds[:,3],Period)
