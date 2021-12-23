
from player import HumanPlayer, RandomComputerPlayer
import time
class TicTacToe:
    def __init__(self, length=3):
        #how create a list with for loop
        self.board = [' ' for _ in range(length*length)] # we will use a single list to rep 3*3 board
        self.length = length
        self.current_winner = None # keep track of winner!

    def print_board(self):
        #sloewst way
        # rows = []
        # for i in range(3):
        #     rows.append(self.board[i*3:(i+1)*3]) 
        # for row in rows:
        #    #string.join(array) example: '.'.join([1,2,3]) => '1.2.3'
        #    print('| ' + ' | '.join(row) + ' |')

        #fastest way
        i=0
        for row in [self.board[i*self.length:(i+1)*self.length] for i in range(self.length)]:
            new_board = []
            for index, value in enumerate(row):
               if value=='X' or value == 'O':
                   new_board.append(value)
               else:
                   new_board.append(str(index+i))
            print('| ' + ' | '.join(new_board) + ' |')
            i+=3


    def print_board_nums(self):
        # 0 | 1 | 3 etc (tells us what number corresponds to what box)
        for row in [[str(i) for i in range(j*self.length, (j+1)*self.length)] for j in range(self.length)]:
            print('| ' + ' | '.join(row) + ' |')


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
        game.print_board_nums()
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
    game = TicTacToe(4)

    play(game, x_player, o_player, True)