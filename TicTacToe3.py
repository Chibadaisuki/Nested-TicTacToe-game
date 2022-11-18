import functools
def TicTacToe():

    PIECE_X = 'X'
    PIECE_O = 'O'
    PIECE_EMPTY = '_'

    class Coordinate:
        def __init__(self, row, column):
            self.row = row
            self.column = column

        def __repr__(self):
            return f'Coordinate(row={self.row},column={self.column})'

    class Game:
        def __init__(self):
            self.size = 9
            self.board = [
                [PIECE_EMPTY for x in range(self.size)]
                for y in range(self.size)
            ]
            self.count = 0
            self.stack = []
            self.win = []
            self.b = [[[0,0,0],[0,0,0],0,0],[[0,0,0],[0,0,0],0,0],[[0,0,0],[0,0,0],0,0],[[0,0,0],[0,0,0],0,0],[[0,0,0],[0,0,0],0,0],[[0,0,0],[0,0,0],0,0],[[0,0,0],[0,0,0],0,0],[[0,0,0],[0,0,0],0,0],[[0,0,0],[0,0,0],0,0]]
            self.bcol = [0,0,0]
            self.brow = [0,0,0]
            self.bant = 0
            self.bdia = 0
            self.restart = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        def get_user_move(self):
            try:
                user = input("Move: ")
                assert (len(user) == 2)
                move = Coordinate(
                    ord(user[0]) - ord('a'),
                    int(user[1]) - 1
                )
                assert (move.row > -1 and move.row < 9)
                assert (move.column > -1 and move.column < 9)
                print()
                return move
            except (KeyboardInterrupt, EOFError) as e:
                exit()
            except:
                print("Invalid input. Format should be like b4\n")
                return self.get_user_move()

        def render(self):
            print("  a b c   d e f   g h i")
            print("\n  ______|_______|______\n        |       |\n".join(
                map(lambda outer_y: "\n".join(
                    map(lambda inner_y: str(outer_y * 3 + inner_y + 1) + " " + " | ".join(
                        map(lambda outer_x: "|".join(
                                    map(
                                        lambda inner_x: self.board[outer_x *
                                                                   3 + inner_x][outer_y * 3 + inner_y],
                                        range(3)
                                    )
                        ), range(3)
                        )
                    ), range(3)
                    )
                ), range(3)
                )
            )
            )
            print()

        def play(self):
            while True:
                self.render()
                move = self.get_user_move()
                pos = int(move.row/3) * 3 + int(move.column/3)
                self.restart[pos] += 1
    
                while self.board[move.row][move.column] != PIECE_EMPTY or pos in self.win:
                        print('error, please resubmit')
                        move = self.get_user_move()
                        pos = int(move.row/3) * 3 + int(move.column/3)                

                if self.count %2 == 0:
                    chose = PIECE_X
                    add = 1
                else:
                    chose = PIECE_O
                    add = -1
                    
                self.count += 1

                self.board[move.row][move.column] = chose
                row = int(move.row)%3
                col = int(move.column)%3
                self.b[pos][0][row] += add
                self.b[pos][1][col] += add

                if move.row%3 == move.column%3:
                    self.b[pos][2] += add
                if move.row%3 + move.column%3 == 2:
                    self.b[pos][3] += add
                if self.b[pos][2] == 3 or self.b[pos][3] == 3 or max(self.b[pos][0]) == 3 or max(self.b[pos][1]) == 3 or self.b[pos][2] == -3 or self.b[pos][3] == -3 or min(self.b[pos][0]) == -3 or min(self.b[pos][1]) == -3:
                    self.win.append(pos)
                    p1 = int(pos%3)
                    p2 = int(pos//3)
                    self.bcol[p1] += add
                    self.brow[p2] += add
                    if p1 == p2:
                        self.bdia += add
                    if p1 + p2 == 2:
                        self.bant += add
                    if max(self.bcol) == 3 or max(self.brow) == 3 or self.bdia == 3 or self.bant == 3:
                        print('X win')
                        return False
                    elif min(self.bcol) == -3 or min(self.brow) == -3 or self.bdia == -3 or self.bant == -3:
                        print('O win')
                        return False
                if self.restart[pos] == 9 and pos not in self.win:
                    self.restart[pos] = 0
                    self.b[pos] = [[0,0,0],[0,0,0],0,0]
                    x = pos%3
                    y = int(pos/3)
                    for i in range(3*x, 3*x+3):
                        for j in range(3*y, 3*y+3):
                            self.board[i][j] = PIECE_EMPTY
                    
    return Game


if __name__ == "__main__":
    print("Nested TicTacToe")
    print("------")
    game = TicTacToe()()
    game.play()
