import random

# Base class
class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter
    
    # We want all players to get the next move given in a game
    # We will define it in the the sub classes
    def get_move(self, game):
        pass

# Sub class of Player
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square

# Sub class of Player
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8) ')
            # Check whether user entered an integer or not => If not, try again
            # If it is an integer, check if that spot is available or not => If not try again
            # If that spot is available i.e valid, return the spot
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val