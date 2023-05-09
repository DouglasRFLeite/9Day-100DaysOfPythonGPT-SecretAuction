import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
clear()

def get_player(players_dict):
    print("Welcome to the Secret Auction!")
    name = input("Tell me your name: ")
    bid = int(input("What is your bid? $"))
    players_dict[name] = bid

    anyone_else = input("Is there anyone else bidding? (answer with Y or N)").lower()

    return players_dict, anyone_else

def find_winner(players_dict):
    max = 0
    for player in players_dict:
        if players_dict[player] >  max:
            max = players_dict[player]
            winner = player
    
    return winner

def secret_auction(): 
    players_dict = {}
    while True:
        players_dict, anyone_else = get_player(players_dict)
        if anyone_else == "n":
            break
        clear()

    print(f"""The winner is {find_winner(players_dict)} \
with a bid of ${players_dict[find_winner(players_dict)]}.""")

if __name__ == "__main__":
    secret_auction()