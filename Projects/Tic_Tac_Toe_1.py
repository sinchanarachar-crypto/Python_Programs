board = [" "] * 9
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
        return False

def is_draw(board):
    return " " not in board

def play_game():
    board = [" "] * 9
    current_player = "X"

    while True:
        print_board(board)

        try:
            move = int(input(f"Player {current_player}, enter position (1 - 9) : ")) - 1

            if move < 0 or move > 8:
                print("Invalid position")
                continue

            if board[move] != " ":
                print("Already Occupied")
                continue

            board[move] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Enter a Valid Number")

play_game()