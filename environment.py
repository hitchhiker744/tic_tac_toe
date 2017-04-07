import numpy as np

class Environment:
    def __init__(self):
        self.board = np.zeros((LENGTH, LENGTH))
        self.x = -1 #represents an x on the board, player 1
        self.o = 1 #represents an o on the board, player 2
        self.winner = None
        self.ended = False
        self.num_states = 3**(LENGTH*LENGTH)

    def is_empty(self, i, j):
        # returns true if [i,j] is empty
        return self.board[i,j] == 0

    def reward(self, symbol):
        # retuns a reward for a specific player
        # no reward until game is over
        if not self.game_over():
            return 0

        # if we get here, game is over# sym will be self.x or self.o
        return 1 if self.winner == symbol else 0

    def get_state(self):
        # hashing the state of the board to a single integer
        '''
        returns the current state, represented as an integer
        from 0 to |S|-1, where S = set of all possible states
        |S| = 3^(board size), since each cell can have 3 possible values:
        empty, x, o
        '''

        k = 0
        h = 0
        for i in range(LENGTH):
            for j in range(LENGTH):
                if self.board[i,j] == 0:
                    v = 0
                elif self.board[i,j] == self.x:
                    v = 1
                elif self.board[i,j] == self.o:
                    v = 2

                h += (3**k) * v
                k += 1
        return h

    def game_over(self, force_recalculate=False):
        # looks at the state of the game and return true or false
        if not force_recalculate and self.ended:
            return self.ended

        CONTINUE_HERE!!!!!

    def draw_board(self):
        # draws the board
        pass
