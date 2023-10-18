def print_board(matrix):
    print(F" {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]} ")
    print("---|---|---")
    print(F" {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]} ")
    print("---|---|---")
    print(F" {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} ")


if __name__ == "__main__":
    matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    print("Welcome to Tic Tac Toe")
    print_board(matrix)
