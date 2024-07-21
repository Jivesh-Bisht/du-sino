import sqlite3 
  
conn = sqlite3.connect('db.db') 
  
cursor = conn.cursor() 

def add_money(amount:int,uid:int):
    mny = curser.execute('SELECT credits FROM players WHERE uid=?',uid)
    newamt=mny+amount
    curser.execute('UPDATE players SET credits=? WHERE uid=? ',newamt,uid)

def remove_money(amount:int,uid:int):
    mny = curser.execute('SELECT credits FROM players WHERE uid=?',uid)
    newamt=mny-amount
    curser.execute('UPDATE players SET credits=? WHERE uid=? ',newamt,uid)