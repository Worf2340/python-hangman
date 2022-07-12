import random
import os
from enum import Enum


def select_word():
    words = open("words.txt", "r").read().splitlines()
    word: str = random.choice(words)
    return word


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class State(Enum):
    PLAYING = 0
    WON = 1
    LOST = 2


class Game:
    def __init__(self):
        self.guesses = []
        self.tries = 5
        self.state = State.PLAYING
        self.word = select_word()
        self.board = ["_" for letter in self.word]

    def guess(self):
        guess: str = input("Guess a letter: ")

        while guess in self.guesses:
            print("You already guessed that letter.")
            guess: str = input("Guess a letter: ")

        if guess in self.word:
            self.update_board(guess)
        else:
            self.tries -= 1
            if self.tries < 1:
                self.state = State.LOST

        self.guesses.append(guess)

    def update_board(self, guess):
        for i in range(0, len(self.word)):
            if self.word[i] == guess:
                self.board[i] = guess

        if "_" not in self.board:
            self.state = State.WON

    def print_board(self):
        print(" ".join(self.board))


def play_game(game):
    print(game.word)

    # Main game loop
    while game.state == State.PLAYING:
        clear_screen()
        print("You have {} tries remaining".format(game.tries))
        game.print_board()
        game.guess()


if __name__ == '__main__':
    clear_screen()
    print("Welcome to Hangman!")
    game = Game()
    play_game(game)
    while game.state == State.PLAYING:
        clear_screen()
        print("You have {} tries remaining".format(game.tries))
        game.print_board()
        game.guess()

    clear_screen()
    if game.state == State.WON:
        game.print_board()
        print("You won!")
    else:
        print("You lost. The word was {}.".format(game.word))

print("")
