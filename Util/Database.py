#!/usr/bin/python

import MySQLdb

class Database:
  def __init__(self, configFile):
    self.__parseConfiguration(configFile)
    self._conn = MySQLdb.connect(self.host,self.username,self.password,self.dbname)
    self._cursor = self._conn.cursor()
    
  def __parseConfiguration(self, configFile):
    noLinesConf = 4
    conf = []
    i = 0
    with open(configFile, "r") as f:
      for line in f:
        conf.append(line)
        
    self.host = conf[0][:len(conf[0])-1]
    self.username = conf[1][:len(conf[1])-1]
    self.password = conf[2][:len(conf[2])-1]
    self.dbname = conf[3][:len(conf[3])-1]

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.commit()
    self.connection.close()

  @property
  def connection(self):
    return self._conn

  @property
  def cursor(self):
    return self._cursor

  def commit(self):
    self.connection.commit()

  def query(self, sql, params=None):
    self.cursor.execute(sql, params or ())

  def fetchall(self):
    return self.cursor.fetchall()

  def fetchone(self):
    return self.cursor.fetchone()
    
if __name__ == '__main__':    
  db = Database("db.conf")
  db.query("select version()")
  version = db.fetchone()
  print(version[0])
