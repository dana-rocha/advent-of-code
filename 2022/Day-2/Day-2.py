'''
Rock, Paper, Scissors

First column: what your opponent is going to play
A = Rock
B = Paper
C = Scissors

Second column: what you should play in response
X = Rock
Y = Paper
Z = Scissors

Your total score = sum of your scores for each round

Score for a round is the 
shape you selected + outcome of 
the round (0 if you lose, 3 for a draw, 6 if you won)
1 = Rock
2 = Paper
3 = Scissors

This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), 
and you should choose Paper (Y). This ends in a win for you 
with a score of 8 (2 because you chose Paper + 6 because you won).

In the second round, your opponent will choose Paper (B), 
and you should choose Rock (X). This ends in a loss for you 
with a score of 1 (1 + 0).

The third round is a draw with both players choosing Scissors, 
giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, 
you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according 
to your strategy guide?
'''
import argparse

def main(infile):
    game_play = process_data(infile)
    score_game(game_play)

def process_data(infile):
    with open(infile) as f:
        games = f.read().split("\n")

    processed_list = []
    for game in games:
        processed_list.append(game.split())
    return(processed_list)

def score_game(game_strategy):
    """
    Score for a round is the 
    shape you selected + outcome of 
    the round (0 if you lose, 3 for a draw, 6 if you won)
    1 = Rock
    2 = Paper
    3 = Scissors
    """
    total = 0

    opponent_rps = {
        "A": "rock",
        "B": "paper",
        "C": "scissors"
    }

    my_rps = {
        "X": "lose",
        "Y": "draw",
        "Z": "win"
    }

    winners = {
        "rock" : "scissors",
        "scissors": "paper",
        "paper" : "rock"
    }

    for game in game_strategy:
        opponent = opponent_rps[game[0]]
        me = my_rps[game[1]]

        if me == "Y":
            # Game has to be a draw
            my_play = opponent
        elif me == "Z":
            # I have to win the game
            # Need to get the key of the winners dictionary
            for key, val in winners.items():
                if val == opponent:
                    my_play = key
                    return my_play
        else:
            # I have to lose the game
            my_play = winners[opponent]

        total += declare_winner(opponent, my_play)

    print (f"Your total score: {total}")

def declare_winner(player1, player2):
    winners = {
        "rock" : "scissors",
        "scissors": "paper",
        "paper" : "rock"
    }

    points = {
        "rock": 1,
        "paper": 2,
        "scissors": 3
    }

    if player1 in winners.keys() and player2 == winners[player1]:
        return 0 + points[player2]
    elif player2 in winners.keys() and player1 == winners[player2]:
        return 6 + points[player2]
    else:
        return 3 + points[player2]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='infile', required=True)
    args = parser.parse_args()
    main(args.infile)