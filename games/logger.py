import sqlite3 
  
conn = sqlite3.connect('logs.db') 
  
cursor = conn.cursor() 

class Logger():
    def log(self,log:str):
        cursor.execute('INSERT INTO logs(logtype,log,uid) VALUES(?,?,1)',('syslog',log))

    def won(self,game:str,amount:int,uid:int ):
        cursor.execute('INSERT INTO logs(logtype,log,uid) VALUES(?,?,?)',('won',f'{uid} won {amount} in {game}',uid))

    def error(self,err:str):
        cursor.execute('INSERT INTO logs(logtype,log,uid) VALUES(?,?,0)',('errlog',err))
