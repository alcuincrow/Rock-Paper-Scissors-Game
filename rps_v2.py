
import random


'''This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round.'''


moves = ['rock', 'paper', 'scissors']
human_move_log = []
cycle_move_log = []

'''The Player class is the parent class for all of the Players
in this game'''


# get valid input for human player class
def valid_input(prompt, options):
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        else:
            print(f'{choice} is invalid, please try again.\n')


# game mechanics.
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# main player class
class Player:

    def move(self):
        self.HumanPlayer
        self.AiPlayer

    def learn(self, my_move, their_move):
        # The pass statement is used to pass the function on to sub classes,
        # because having an empty function isn't legal in python
        pass


# subclass of player for random actions
class RandomPlayer(Player):
    def move(self):
        moves = ['rock', 'paper', 'scissors']
        move = random.choice(moves)
        return move


# human player class
class HumanPlayer(Player):
    def move(self):
        move = valid_input('Type your move choice\n', [
                           'rock', 'paper', 'scissors'])
        human_move_log.append(move)
        return move


# was raised under a rock, and only knows about rocks
class RockPlayer(Player):
    def move(self):
        my_move = 'rock'
        return my_move


# reflect player class
class ReflectPlayer(Player):
    def move(self):
        try:
            human_move_log[1]
        except IndexError:
            return 'rock'
        else:
            return human_move_log[-2]


# cycle player class, repeats moves in order, forever
class CyclePlayer(Player):
    def move(self):
        try:
            cycle_move_log[0]
        except IndexError:
            cycle_move_log.append('rock')
            return 'rock'
        else:
            print(cycle_move_log)
            if cycle_move_log[-1] == 'rock':
                cycle_move_log.append('paper')
                return 'paper'
            elif cycle_move_log[-1] == 'paper':
                cycle_move_log.append('scissors')
                return 'scissors'
            elif cycle_move_log[-1] == 'scissors':
                cycle_move_log.append('rock')
                return 'rock'


# game class for controlling the game
class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    # used to pick the number of rounds
    def rounds(self):
        number_of_rounds = int(valid_input('Pick the number of rounds to play:'
                               '1 or 3 or 5\n', ['1', '3', '5']))
        for rounds in range(number_of_rounds):
            print('Round start!')
            if rounds != number_of_rounds:
                self.play_round()

    # round mechanics

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f'\nPlayer 1: {move1}\nPlayer 2: {move2}')
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            self.p1_score += 1
            print(f"Player 1 wins!")
        elif beats(move2, move1):
            self.p2_score += 1
            print(f"Player 2 wins!")
        else:
            print("It was a tie.")
        print(f'\nPlayer 1 Score: {self.p1_score}\n'
              f'Player 2 Score: {self.p2_score}\n')

    # tracks scores for the players each round
    def results(self):
        print('FINAL SCORE:')
        print(f'Player 1 Score: {self.p1_score}\n'
              f'Player 2 Score: {self.p2_score}\n')
        if self.p1_score > self.p2_score:
            print("You're the winner!")
        elif self.p1_score < self.p2_score:
            print('You lose!')
        else:
            print('Tie')

    # function for running the game
    def play_game(self):
        print('Game start!')
        self.rounds()
        self.results()
        print('Game over!')


# runs the program
if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
