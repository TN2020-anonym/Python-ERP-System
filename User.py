#!/usr/bin/python

from Util.Database import Database

class User:
  def __init__(self, username, password):    
    g_db.query("select role from user where username = '" + username + "' and password = '" + password + "'")
    result = g_db.fetchone()    
    
    if result == None:
      print("user does not exist")
      raise 
      
    self.username = username
    self.role = result[0]    
    
  @classmethod
  def createNewUser(self, username, password, role):
    g_db.query("insert into user (username, password, role) "\
               " values ('" + username + "', '" + password + "', '" + role + "')")    
  
  @classmethod
  def deleteUser(self, username, password):
    g_db.query("delete from user where username = '" + username + "' and password = '" + password + "'")

if __name__ == '__main__':
  g_db = Database("./Util/db.conf")
  g_db.query("select * from user")
  result = g_db.fetchall()
  print(result)
  
  
  