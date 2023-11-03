from random import randint

# make me a video game
def create_game():
    """
    Create a game of battleship
    """
    # create a board
    board = []
    for x in range(5):
        board.append(["O"] * 5)
    # print the board
    def print_board(board):
        for row in board:
            print(" ".join(row))
    print_board(board)
    # create a ship
    def random_row(board):
        return randint(0, len(board) - 1)
    def random_col(board):
        return randint(0, len(board[0]) - 1)
    ship_row = random_row(board)
    ship_col = random_col(board)
    # print(ship_row)
    # print(ship_col)
    # print(board[ship_row][ship_col])
    # start the game
    for turn in range(4):
        print("Turn", turn + 1)
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))
        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sank my battleship!")
            break
        else:
            if guess_row not in range(5) or \
               guess_col not in range(5):
                print("Oops, that's not even in the ocean.")
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
            if turn == 3:
                print("Game Over")
            print_board(board)
    # print(board)
    # print(board[0][0])
    # print(board[1][0])
    # print(board[2][0])
    # print(board[3][0])
    # print(board[4][0])
    # print(board[0][1])
    # print
create_game()