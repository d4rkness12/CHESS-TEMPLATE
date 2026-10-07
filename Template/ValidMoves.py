
class ValidMoves:

    @staticmethod
    def knight_valid_moves(board, start, end):
        start_x, start_y = start
        end_x, end_y = end

        x_diff = abs(start_x - end_x)
        y_diff = abs(start_y - end_y)

        return  (
            (x_diff == 2 and y_diff == 1) or 
            (x_diff == 1 and y_diff == 2)
        )

    @staticmethod
    def rook_valid_moves(board, start, end):
        start_x, start_y = start
        end_x, end_y = end

        if start_x == end_x:
            for i in range(min(start_y, end_y) + 1, max(start_y, end_y)):
                index = start_x * 8 + i

                if board[index] != ".":
                    return False


        elif start_y == end_y:
            for i in range(min(start_x, end_x) + 1, max(start_x, end_x)):
                index = i * 8 + start_y

                if board[index] != ".":
                    return False

        else:
            return False
        
        return True

    @staticmethod
    def bishop_valid_moves(board, start, end):
        start_x, start_y = start
        end_x, end_y = end

        if start == end:
            return False

        x_diff = abs(start_x - end_x)
        y_diff = abs(start_y - end_y)

        if x_diff != y_diff:
            return False

        x_direction = 1 if end_x > start_x else -1
        y_direction = 1 if end_y > start_y else -1

        for i in range(1, x_diff):
            x = start_x + i * x_direction
            y = start_y + i * y_direction

            index = x * 8 + y

            if board[index] != ".":
                return False

        return True

    @staticmethod
    def queen_valid_moves(board, start, end):

        return (
            ValidMoves.rook_valid_moves(board, start, end) or
            ValidMoves.bishop_valid_moves(board, start, end)
        )

    @staticmethod
    def king_valid_moves(board,start,end) :

        start_x, start_y = start
        end_x, end_y = end

        x_diff = abs(start_x - end_x)
        y_diff = abs(start_y - end_y)

        return (
            x_diff <= 1
            and y_diff <= 1
            and (x_diff, y_diff) != (0, 0)
        )

    @staticmethod
    def pawn_valid_moves(board, start, end, color):
        start_x, start_y = start
        end_x, end_y = end

        direction = -1 if color == "white" else 1
        start_row = 6 if color == "white" else 1

        x_diff = end_x - start_x
        y_diff = abs(end_y - start_y)

        if y_diff == 0 and x_diff == direction:
            return board[end_x * 8 + end_y] == "."

        if y_diff == 0 and x_diff == 2 * direction:
            middle = (start_x + direction) * 8 + start_y
            destination = end_x * 8 + end_y

            return (
                start_x == start_row
                and board[middle] == "."
                and board[destination] == "."
            )

        if y_diff == 1 and x_diff == direction:
            destination = end_x * 8 + end_y

            return board[destination] != "."

        return False