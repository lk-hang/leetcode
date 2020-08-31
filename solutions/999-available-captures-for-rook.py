"""

On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.


"""

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for row in range(8):
            for col in range(8):
                if board[row][col] == 'R':
                    row_R, col_R = row, col
                    break

        count = 0
        for row_idx, col_idx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            row, col = row_R + row_idx, col_R + col_idx
            while (0 <= row < 8) and (0 <= col < 8):
                if board[row][col] == 'p':
                    count += 1
                    break
                elif board[row][col] == 'B':
                    break
                row, col = row + row_idx, col + col_idx
        return count
