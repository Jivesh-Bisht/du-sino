import json 
from flask import Flask, jsonify, request
from games.russian_roulette import roulette
from games.rps import rps
from games.helper import add_money,remove_money

app = Flask(__name__) 


@app.route('/balance', methods = ['GET']) 
def balance(): 
    uid = request.args.get('uid')
    balance = 0 # add balance
    return balance

@app.route('/russian_roulette', methods = ['GET']) 
def russian_roulette(): 
    uid = request.args.get('uid')
    amount=request.args.get('amount')
    res = roulette(amount,uid)
    return {"won":res}

@app.route('/rps', methods = ['GET']) 
def rps(): 
    uid = request.args.get('uid')
    amount=request.args.get('amount')
    choice=request.args.get('choice')
    res = rps(amount,uid,choice)
    if res["result"]=="won":
        add_money(amount,uid)
    else:
        remove_money(amount,uid)

    return res

@app.route('/signup',methods = ['POST'])
def signup():
    id=request.args.get('id')
    email=request.args.get('email')
    username=request.args.get('username')
    password=request.args.get('password')
    
    # add this shit to db

if __name__ == '__main__': 
    app.run(debug=True, port=6969)