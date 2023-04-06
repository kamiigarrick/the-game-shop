import random
import time


def yahtzee():
    # automatic timer for the game to start
    countdown = 3
    for i in range(countdown, 0, -1):
        print(i)
        time.sleep(1)

    print("GO, LETS PLAY YAHTZEE!!!")
    print()

    def roll_dice():
        rolls = []
        for i in range(5):
            rolls.append(random.randint(1, 6))
        return rolls

    players = []
    for i in range(4):
        name = input("Please enter " + str(i + 1) + "your name: ")
        players.append(name)
    print()

    scores = [0, 0, 0, 0]
    for i in range(3):
        print("Round", i + 1, "of 3:")
        for k in range(4):
            print(players[k], "Your turn to roll the dice!!")
            dice = roll_dice()
            print("You rolled:", dice)
            if len(set(dice)) == 3:
                for value in set(dice):
                    if dice.count(value) == 3:
                        print("YAHTZEE !!! You rolled three", value, "s")
                        scores[k] += 40
                        break
            else:
                print("NO YAHTZEE!")
            print(players[k], "Score is now", scores[k])
            print()

    max_score = max(scores)
    max_index = scores.index(max_score)
    min_score = min(scores)
    min_index = scores.index(min_score)

    print(players[max_index], "CONGRATULATIONS !!!! YOU WON WITH A SCORE OF", max_score, "!!")
    print(players[min_index], "SORRY YOU LOST THE GAME WI1TH A SCORE OF", min_score)


def ludo():
    class Ludo:
        def __init__(self):
            self.board = [0] * 52
            self.players = []
            self.current_player = None
            self.current_roll = None
            self.current_piece = None
            self.num_pieces = 4
            self.num_players = None

        def roll_dice(self):
            return random.randint(1, 6)

        def add_player(self, player_name):
            self.players.append(player_name)

        def start_game(self):
            print('Starting Ludo game...')
            self.current_player = random.choice(self.players)

        def play_game(self):
            while not self.num_players:
                num_players = int(input('Enter number of players (max 4): '))
                if num_players > 4:
                    print('The maximum number of players is 4. Please enter a valid number.')
                else:
                    self.num_players = num_players

            for i in range(self.num_players):
                player_name = input(f'Enter name of player {i + 1}: ')
                self.add_player(player_name)

            self.start_game()

            while True:
                for player in self.players:
                    self.current_player = player
                    print(f"{self.current_player}'s turn!")
                    input('Press enter to roll the dice...')
                    self.current_roll = self.roll_dice()
                    print(f'{self.current_player} rolled {self.current_roll}!')
                    if self.current_roll == 6:
                        print(f'{self.current_player} rolled a six! Placing a piece on the board...')
                        pieces = [i for i, x in enumerate(self.board) if x == 0]
                        if pieces and self.num_pieces > 0:
                            self.current_piece = min(pieces)
                            print(f'Placing piece {self.num_pieces} for {self.current_player} on position {self.current_piece}')
                            self.board[self.current_piece] = self.current_player
                            self.num_pieces -= 1
                        else:
                            print('No more pieces left!')
                    pieces = [i for i, x in enumerate(self.board) if x == self.current_player]
                    if pieces:
                        self.current_piece = random.choice(pieces)
                        new_position = (self.current_piece + self.current_roll) % 52
                        if new_position < self.current_piece:
                            new_position = self.current_piece + self.current_roll
                        if new_position < 52 and self.board[new_position] == 0:
                            print(f'Moving piece {self.current_piece} to position {new_position}')
                            self.board[self.current_piece] = 0
                            if self.board[new_position] != 0:
                                print('yuh dead')
                            self.board[new_position] = self.current_player
                            if new_position == 51:
                                print(f'{self.current_player} wins!')
                                return

    ludo = Ludo()
    ludo.play_game()


def cactus_jack():
    class CactusJack:
        def __init__(self):
            self.user_score = 0
            self.game_count = 0

        def roll_dice(self):
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            return die1, die2

        def play(self):
            self.game_count += 1
            print("\nStarting a new game of Cactus Jack...")

            input("Press Enter to roll the dice...")
            die1, die2 = self.roll_dice()
            roll_sum = die1 + die2
            print(f"\nYou rolled a {die1} and a {die2}. Total: {roll_sum}")

            if roll_sum in [7, 11]:
                print("Congratulations! You won!")
                self.user_score += 1
            elif roll_sum in [2, 3, 12]:
                print("Sorry, you lost.")
            else:
                point = roll_sum
                print(f"Your point is {point}. Keep rolling until you get {point} or 7.")

                while True:
                    input("Press Enter to roll the dice again...")
                    die1, die2 = self.roll_dice()
                    roll_sum = die1 + die2
                    print(f"\nYou rolled a {die1} and a {die2}. Total: {roll_sum}")

                    if roll_sum == point:
                        print("Congratulations! You won!")
                        self.user_score += 1
                        break
                    elif roll_sum == 7:
                        print("Sorry, you lost.")
                        break

            print(f"\nYour current score: {self.user_score}")
            print(f"Games played: {self.game_count}")
            print(f"Average score: {self.user_score / self.game_count}")

    game = CactusJack()
    game.play()


if __name__ == "__main__":
    while True:
        print("\nWelcome to the Jamaican Game Hub!")
        print("1. Yahtzee")
        print("2. Ludo")
        print("3. Cactus Jack")
        print("4. Quit")
        choice = input("Please enter the number corresponding to the game you'd like to play: ")

        if choice == '1':
            yahtzee()
        elif choice == '2':
            ludo()
        elif choice == '3':
            cactus_jack()
        elif choice == '4':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")