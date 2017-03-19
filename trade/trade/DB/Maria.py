# -*- coding: utf-8 -*-
"""
Created on Sun May  8 16:27:07 2016

@author: salem7mg
"""

import MySQLdb
class Maria:
  def connect(self) : 
    self.connector =  MySQLdb.connect(host="salem7mg-on-lubuntu", db="fxt", user="root", passwd="techpwd1862", charset="utf8")
    self.connector.autocommit(False)
    return self.connector 
  def inquire(self,sql):
    cursor = self.connector.cursor()
    cursor.execute(sql)
    records = cursor.fetchall()
    return records
  def dml(self,sql):
    cursor = self.connector.cursor()
    cursor.execute(sql)
    self.connector.commit()
    cursor.close()
    connector.close()
    return
  def close(self):  
    self.close
    return  