import random 

def play():
    user = input("'r' for rock, 'p' for paper and 's' for scissors:").lower()

    computer = random.choice(['r','p','s'])

    if user == computer:
        return "empate"
    if is_win(user, computer) :
        return "ganhou"
    else:
        return "perdeu"
    
def is_win(player1, player2):
    if (player1 == 'r' and player2 == 's') or (player1 == 'p' and player2 == 'r') or (player1 == 's' and player2 == 'p'):
        return True
    return False

