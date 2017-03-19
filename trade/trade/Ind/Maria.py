# -*- coding: utf-8 -*-
"""
Created on Sun May  8 16:27:07 2016

@author: salem7mg
"""

import MySQLdb
import pandas.io.sql as psql
class Maria:
  def inquire(self,sql):
    connector =  MySQLdb.connect(host="salem7mg-on-lubuntu", db="fxt", user="root", passwd="techpwd1862", charset="utf8")
    cursor = connector.cursor()
    cursor.execute(sql)
    records = list(cursor.fetchall())
    cursor.execute("unlock tables;")
    cursor.close()
    connector.close()
    return records
  def inquireDf(self,sql):
    connector =  MySQLdb.connect(host="salem7mg-on-lubuntu", db="fxt", user="root", passwd="techpwd1862", charset="utf8")
    cursor = connector.cursor()
    cursor.execute(sql)
    records = psql.read_sql(sql, connector)
    cursor.execute("unlock tables;")
    cursor.close()
    connector.close()
    return records
  def dml(self,sql):
    connector =  MySQLdb.connect(host="salem7mg-on-lubuntu", db="fxt", user="root", passwd="techpwd1862", charset="utf8")
    connector.autocommit(False)
    cursor = connector.cursor()
    cursor.execute(sql)
    connector.commit()
    cursor.close()
    connector.close()
    return
  def close(self):  
    self.close
    return  