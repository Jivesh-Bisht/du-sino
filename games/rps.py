import random
from logger import Logger
choices = ["rock","paper","scissor"]

def rps(amount:int,uid:int,choice):
    comp = random.choice(choices)
    user_action=choice
    computer_action=comp
    
    if choice in choices:
        if comp==choice:
            Logger.won(game='rps',amount=0,uid=uid)
            return {"result":"draw","comp":comp}

        elif user_action == "rock":
            if computer_action == "scissors":
                return {"result":"win","comp":comp}
                Logger.won(game='rps',amount=amount,uid=uid)
            else:
                return {"result":"lost","comp":comp}
                Logger.lost(game='rps',amount=amount,uid=uid)

        elif user_action == "paper":
            if computer_action == "rock":
                return {"result":"win","comp":comp}
                Logger.won(game='rps',amount=amount,uid=uid)
            else:
                return {"result":"lost","comp":comp}
                Logger.lost(game='rps',amount=amount,uid=uid)

        elif user_action == "scissors":
            if computer_action == "paper":
                return {"result":"win","comp":comp}
                Logger.won(game='rps',amount=amount,uid=uid)
            else:
                return {"result":"lost","comp":comp}
                Logger.lost(game='rps',amount=amount,uid=uid)


    return True


