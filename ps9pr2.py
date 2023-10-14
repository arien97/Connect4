#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.

class Player:
    
    def __init__(self, checker):
        """ constructs a new Player object
        """
        
        assert(checker == 'X' or checker == 'O')
        
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """ returns a string representing a Player object
        """
        
        s = "Player " + self.checker
        
        return s
    
    def opponent_checker(self):
        """ returns a one-character string representing the checker of the
            Player object's opponent
        """
        
        if self.checker == 'O':
            return 'X'
        else:
            return 'O'
        
        
    def next_move(self, b):
        """ that accepts a Board object b as a parameter and retuurns the
            column where the player wants to make the next move
        """
        self.num_moves += 1
        
        while True:
            col = int(input("Enter a column: "))
            if b.can_add_to(col) == True:
                return col
            else:
                print('Try again!' + '\n')
        