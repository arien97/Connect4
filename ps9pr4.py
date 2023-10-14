#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """ an "intelligent" computer player that uses techniques from
        artificial intelligence    
    """
    
    def __init__(self, checker, tiebreak, lookahead):
        """ constructor that inherits attributes from the Player class
            and with attriubutes checker, tiebreak, and lookahead
        """
        
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
        
    def __repr__(self):
        """ returns a string representing an AIPlayer object
        """
        
        s = "Player " + self.checker + " (" + self.tiebreak + ", " + str(self.lookahead) + ")"
        return s
    
    
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the board,
            and returns the index of the column with the max score. If one or more
            columns are tied for the maximum score, the method should apply the called
            AIPlayer's tiebreaking strategy to break the tie
        """
        
        max_scores = max(scores)
        index_list = []
        
        for i in range(len(scores)):
            if scores[i] == max_scores:
                index_list += [i]
                
        if self.tiebreak == 'LEFT':
            return index_list[0]
        elif self.tiebreak == 'RIGHT':
            return index_list[-1]
        else:
            return random.choice(index_list)
        
        
    def scores_for(self, b):
        """ takes a Board object b and determines the called AIPlayer's score for the
            columns in b. Each column is assigned one of 4 possible scores based on 
            the AIPlayer's lookahead value. Returns a list containing one score for each
            column
        """
        
        scores = [25] * b.width
        
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.checker) == False and b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(b)
                if max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 50:
                    scores[col] = 50
                else:
                    scores[col] = -1
                b.remove_checker(col)
                
        return scores
        
        
    def next_move(self, b):
        """ overrides the next_move method that is inherited from Player. Returns the
            AIPlayer's judgement of its best possible move
        """
        
        self.num_moves += 1
        scores = self.scores_for(b)
        col = self.max_score_column(scores)
        
        return col
        
        
        
        