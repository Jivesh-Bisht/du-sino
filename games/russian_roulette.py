import random

def roulette(amount:int,uid:int) -> bool:
    """
    odd position: player
    even position:computer
    """
    
    choice = random.choice([1,2,3,4,5,6],[23,9,23,11,23,11])
    if choice in [2,4,6]:
        return True
    else:
        False
    
"add concept of removing/adding currency"
