import random
from logger import Logger
from helper import add_money,remove_money


def roulette(amount:int,uid:int) -> bool:
    """
    odd position: player
    even position:computer
    """
    
    choice = random.choice([1,2,3,4,5,6],[23,9,23,11,23,11])

    if choice in [2,4,6]:
        add_money(amount,uid)
        Logger.won(game='roulette',amount=amount,uid=uid)
        return {"won":True,"bullet":choice}
    else:
        remove_money_moeny(amount,uid)
        Logger.lost(game='roulette',amount=amount,uid=uid)
        {"won":False,"bullet":choice}

