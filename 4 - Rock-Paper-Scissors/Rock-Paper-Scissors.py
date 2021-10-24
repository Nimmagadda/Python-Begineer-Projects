import random

def play():
    player_score = 0
    comp_score = 0
    print('\nLet\'s play best of five Rock Paper Scissors \n')
    for i in range(5): 
        inp = input("Pick rock(r), paper(p) or scissors(s) : ").lower()
        comp = random.choice(['r','p','s'])
        print(f"\nYou chose {inp} and computer chose {comp} \n")
        if inp == comp:
            print ('It is a tie \n')
            print(f"Score: You {player_score} - {comp_score} Computer \n")
        elif is_win(inp, comp):
            print('You win!! \n')
            player_score=player_score+1
            print(f"Score: You {player_score} - {comp_score} Computer \n")
        else:
            print('Computer Wins!! \n')
            comp_score = comp_score + 1
            print(f"Score: You {player_score} - {comp_score} Computer \n")       
    if comp_score > player_score:
        print(f"You lost best of five {player_score} - {comp_score}\n")
    elif player_score > comp_score: 
        print(f"You win best of five {player_score} - {comp_score} \n") 
    else:
        print("It's a tie \n")


def is_win(player, computer):
    if (player == 'r' and computer =='s') or  (player == 's' and computer =='p') \
        or (player == 'p' and computer =='r'):
        return True

while True:
    ask=input("\nHey, do you want to play a game of Rock Paper Scissors with me? y|n :").lower()
    if ask == 'y':
        play()
    if ask == 'n':
        print("Ok bye, see you later!!")
        break     