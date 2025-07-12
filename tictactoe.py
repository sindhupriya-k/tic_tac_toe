def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    if all([board[i][i] == player for i in range(3)]):  # Check main diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Check anti-diagonal
        return True
    return False


def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    player_idx = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not is_board_full(board):
        current_player = players[player_idx]
        print(f"Player {current_player}, it's your turn.")

        while True:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                break
            print("Invalid move. Try again.")

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        player_idx = 1 - player_idx  # Switch to the other player

    if is_board_full(board):
        print("It's a draw!")


if __name__ == "__main__":
    play_tic_tac_toe()
