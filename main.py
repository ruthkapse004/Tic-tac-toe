def print_board(matrix):
    print(F" {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]} ")
    print("---|---|---")
    print(F" {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]} ")
    print("---|---|---")
    print(F" {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} ")


if __name__ == "__main__":
    matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    turn = 1

    print("Welcome to Tic Tac Toe")
    print_board(matrix)

    while (True):
        if turn:
            print("X's turn")
            x, y = map(int, input("Enter the position (x,y): ").split(","))

            matrix[x-1][y-1] = "X"
            print_board(matrix)

        else:
            print("0's turn")
            x, y = map(int, input("Enter the position (x,y): ").split(","))

            matrix[x-1][y-1] = "0"
            print_board(matrix)
        turn = 1-turn
