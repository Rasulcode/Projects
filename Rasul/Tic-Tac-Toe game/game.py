# Tic-Tac-Toe

# Lövhəni print etmək üçün
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Qalibiyyəti yoxlamaq üçün
def check_win(board, player):
    # Sətirləri yoxlayır
    for row in board:
        if all(mark == player for mark in row):
            return True

    # Sütunları yoxlayır
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Diaqonalları yoxlayır
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

# Oynamaq üçün funksiya
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()
