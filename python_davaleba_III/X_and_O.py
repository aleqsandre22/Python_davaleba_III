import random

BOARD_SIZE = 4

WINNING_LINES = (
    [[(c, r) for c in range(BOARD_SIZE)] for r in range(BOARD_SIZE)]
    + [[(r, c) for c in range(BOARD_SIZE)] for r in range(BOARD_SIZE)]
    + [
        [(c, c) for c in range(BOARD_SIZE)],
        [(r, c) for c, r in enumerate(range(BOARD_SIZE - 1, -1, -1))],
    ]
)


def create_new_board():
    return [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]


def render_board(board):
    print("     c:1 c:2 c:3 ")
    print("    +---+---+---+")
    for r, row in enumerate(board, 1):
        print("r:{row} | {} | {} | {} |".format(*row, row=r))
        print("    +---+---+---+")
    print("")


def get_player_letters():
    player1 = ""
    while player1 not in ("X", "O"):
        player1 = input("Enter player 1 letter (X or O): ").upper()
    player2 = "X" if player1 == "O" else "O"
    return player1, player2


def who_begins(player1, player2):
    return (player1, player2) if random.randint(0, 1) == 0 else (player2, player1)


def make_player_move(board, player):

    while True:
        r = ""
        error = ""
        while True:
            try:
                r = int(
                    input(
                        "{error_text}Player{} please enter row: 1, 2 or 3 (your letter is {}): ".format(
                            *player, error_text=error
                        )
                    )
                )
                if r not in (1, 2, 3):
                    raise
                else:
                    break
            except:
                error = "Invalid input; "
                continue

        c = ""
        while True:
            try:
                c = int(
                    input(
                        "{error_text}Player{} please enter column: 1, 2 or 3 (your letter is {}): ".format(
                            *player, error_text=error
                        )
                    )
                )
                if c not in (1, 2, 3):
                    raise
                else:
                    break
            except:
                error = "Invalid input; "
                continue

        if board[r - 1][c - 1] == " ":
            break
        else:
            print(f"Cell (row:{r},column:{c}) is not empty please choose another one")

    board[r - 1][c - 1] = player[1]


def board_is_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False

    else:
        return True


def get_winner(board):
    for line in WINNING_LINES:
        line_values = [board[r][c] for (r, c) in line]
        if len(set(line_values)) == 1 and line_values[0] != " ":
            return line_values[0]

    return None


def run_session(players):
    board = create_new_board()
    render_board(board)

    i = 0
    while True:
        i += 1
        player = players[i % 2]
        make_player_move(board, player)

        render_board(board)

        if get_winner(board) is not None:
            print("PLAYER{} [{}] WINS\n".format(*player))
            break

        if board_is_full(board):
            print("IT'S A TIE!\n")
            break


def run():
    player1, player2 = [
        (i, player_letter) for i, player_letter in enumerate(get_player_letters(), 1)
    ]
    players = who_begins(player1, player2)
    while True:
        run_session(players)

        whats_next = None
        while whats_next not in (0, 1):
            try:
                whats_next = int(input("Enter 1 - For New Game or 0 - To Quit: "))
            except:
                continue

        if whats_next == 0:
            break


if __name__ == "__main__":
    run()


