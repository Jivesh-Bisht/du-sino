import random

choices = ["rock","paper","scissor"]

def rps(amount:int,uid:int,choice):
    comp = random.choice(choices)
    user_action=choice
    computer_action=comp
    if choice in choices:
        if comp==choice:
            return {"result":"draw","comp":comp}
        elif user_action == "rock":
            if computer_action == "scissors":
                return {"result":"win","comp":comp}
            else:
                return {"result":"lost","comp":comp}
        elif user_action == "paper":
            if computer_action == "rock":
                return {"result":"win","comp":comp}
            else:
                return {"result":"lost","comp":comp}
        elif user_action == "scissors":
            if computer_action == "paper":
                return {"result":"win","comp":comp}
            else:
                return {"result":"lost","comp":comp}


    return True


