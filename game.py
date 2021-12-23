
from player import HumanPlayer, RandomComputerPlayer
import time
class TicTacToe:
    def __init__(self, length=3):
        lengt = 9 if length>9 else int(length)
        #how create a list with for loop
        self.board = [' ' for _ in range(length*length)] # we will use a single list to rep 3*3 board
        self.length = length
        self.current_winner = None # keep track of winner!

    def print_board(self):
        for index, value in enumerate(self.board):
            if index<10:
                print(str(index)+" ", end=" | ")
            else:
                print(index, end=" | ")
            if (index+1) % 9 == 0 :
                print()#next line

    #give me free space in board
    def available_moves(self):
        #enumerate( ['x',' ',' ','o', ...] ) == [(0, 'x'), (1, ' '), (2, ' '), (3, 'o'), ...]
        return [index for index, value in enumerate(self.board) if value == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board # ' ' exists in board or not

    def num_empty_suares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    def winner(self, square, letter):
        row_index = square // 3
        row = self.board[row_index * 3 : (row_index + 1) * 3]
        if all(space == letter for space in row ):
            return True

        col_index = square % 3
        column =[self.board[col_index+i*3] for i in range(3)]
        if all(space == letter for space in column ):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all(space == letter for space in diagonal1 ):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all(space == letter for space in diagonal2 ):
                return True
        return False
        

        


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board()
    letter = 'X' #starting letter
    # iterate while the game still has empty suares
    # (we don't have to worry about winner because we'll just return that
    # which breaks the loop)

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game:
                print(letter+ f' makes a move to square {square}')
                game.print_board()
                print('') #just empty line
            if game.current_winner:
                if print_game:
                    print(letter+ ' wins!!')
                return letter
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(1)
    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = HumanPlayer('O')
    game = TicTacToe(9)

    play(game, x_player, o_player, True)