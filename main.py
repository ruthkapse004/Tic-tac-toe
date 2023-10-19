from random import choice


def print_board(matrix):
    print(F" {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]} ")
    print("---|---|---")
    print(F" {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]} ")
    print("---|---|---")
    print(F" {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} ")


def check_winner(matrix):
    win = None

    if (matrix[0][0] == matrix[1][1] == matrix[2][2] != " "):
        win = matrix[0][0]
        return win

    if (matrix[0][2] == matrix[1][1] == matrix[2][0] != " "):
        win = matrix[0][2]
        return win

    for i in range(3):
        if (matrix[i][0] == matrix[i][1] == matrix[i][2] != " "):
            win = matrix[i][0]
            return win

        if (matrix[0][i] == matrix[1][i] == matrix[2][i] != " "):
            win = matrix[0][i]
            return win

    for i in range(3):
        for j in range(3):
            if matrix[i][j] == " ":
                return win

    return -1


if __name__ == "__main__":
    matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    turn = choice((0, 1))

    print("Welcome to Tic Tac Toe")
    print_board(matrix)

    while (True):
        if turn:
            print("X's turn")
            x, y = list(
                map(int, input("Enter the position (x,y): ").split(",")))
            if (matrix[x-1][y-1] != " "):
                print(F"Position is already marked by '{matrix[x-1][y-1]}'.")
                continue
            matrix[x-1][y-1] = "X"

        else:
            print("0's turn")
            x, y = list(
                map(int, input("Enter the position (x,y): ").split(",")))
            if (matrix[x-1][y-1] != " "):
                print(F"Position is already marked by '{matrix[x-1][y-1]}'.")
                continue
            matrix[x-1][y-1] = "0"

        print_board(matrix)

        winner = check_winner(matrix)
        if (winner == -1):
            print("Match Tie!")
            break

        if (winner):
            print(f"{winner} Wins!")
            break

        turn = 1-turn
