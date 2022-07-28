import traceback


def create_board(new_board_x, new_board_y, new_knight_x, new_knight_y):
    new_board = []
    for y in range(0, new_board_y):
        row = ["O"] * new_board_x
        new_board.append(row)
    new_board[new_board_y - new_knight_y][new_knight_x - 1] = "X"
    return new_board


def print_board(current_knight_x, current_knight_y):
    print_border()
    for y in range(0, len(board)):
        print(str(board_y - y) + "| ", end="")
        for x in range(0, len(board[y])):
            if board[y][x] == "X":
                print((cell_size - 1) * " " + "X ", end="")
            elif board[y][x] == "*":
                print((cell_size - 1) * " " + "* ", end="")
            elif (y == current_knight_y + 2 and (x == current_knight_x + 1 or x == current_knight_x - 1)) or \
                    (y == current_knight_y + 1 and (x == current_knight_x + 2 or x == current_knight_x - 2)) or \
                    (y == current_knight_y - 2 and (x == current_knight_x + 1 or x == current_knight_x - 1)) or \
                    (y == current_knight_y - 1 and (x == current_knight_x + 2 or x == current_knight_x - 2)):
                moves = calculate_moves(x, y)
                available_moves.append([y, x])
                print(((cell_size - 1) * " ") + str(moves) + " ", end="")
            else:
                print(cell_size * "_" + " ", end="")
        print("|")
    print_border()
    print_lower_border_numbers()
    print()


def calculate_moves(knight_new_x, knight_new_y):
    calculate_board = create_board(board_x, board_y, knight_new_x + 1, knight_new_y + 1)
    calculate_board[board_y - knight_new_y - 1][knight_new_x - 1] = "X"
    possible_moves = 0
    for y in range(0, len(board)):
        for x in range(0, len(board[y])):
            if (y == knight_new_y + 2 and (x == knight_new_x + 1 or x == knight_new_x - 1)) or \
                    (y == knight_new_y + 1 and (x == knight_new_x + 2 or x == knight_new_x - 2)) or \
                    (y == knight_new_y - 2 and (x == knight_new_x + 1 or x == knight_new_x - 1)) or \
                    (y == knight_new_y - 1 and (x == knight_new_x + 2 or x == knight_new_x - 2)):
                if calculate_board[y][x] != "X" and board[y][x] != "*" and board[y][x] != "X":
                    possible_moves += 1
                    calculate_board[y][x] = "X"
    return possible_moves


def print_border():
    print(" " + (board_x * (cell_size + 1) + 3) * "-")


def print_lower_border_numbers():
    print("  ", end="")
    for i in range(1, board_x + 1):
        print(cell_size * " " + str(i), end="")


def check_x_y(coordinates, x, y):
    if len(coordinates) != 2:
        print("Invalid dimensions!")
        return False
    if x < 1 or y < 1:
        print("Invalid dimensions!")
        return False
    return True


def check_if_correct_knight_coordinates(board_x, board_y, knight_x, knight_y):
    if knight_x > board_x or knight_y > board_y:
        print("Invalid dimensions!")
        return False
    return True


def count_cell_size(x, y):
    total_cells = x * y
    return len(str(total_cells))


available_moves = []
moves = []
win_counter = 1

while True:
    try:
        while True:
            board_dimensions = input("Enter your board dimensions: ").split()
            board_x = int(board_dimensions[0])
            board_y = int(board_dimensions[1])
            if check_x_y(board_dimensions, board_x, board_y):
                break

        while True:
            starting_coordinates = input("Enter the knight's starting position: ").split()
            knight_x = int(starting_coordinates[0])
            knight_y = int(starting_coordinates[1])
            if check_x_y(starting_coordinates, knight_x, knight_y) and \
                    check_if_correct_knight_coordinates(board_x, board_y, knight_x, knight_y):
                break

        board = create_board(board_x, board_y, knight_x, knight_y)
        cell_size = count_cell_size(board_x, board_y)

        old_x = knight_x - 1
        old_y = board_y - knight_y

        while True:
            if old_x == knight_x - 1 and old_y == board_y - knight_y:
                print_board(old_x, old_y)
            next_move = input("Enter your next move:").split()
            next_x = int(next_move[0]) - 1
            next_y = board_y - int(next_move[1])
            if [next_y, next_x] not in available_moves:
                print("Invalid move! Enter your next move: ")
                continue

            board[next_y][next_x] = "X"
            board[old_y][old_x] = "*"
            win_counter += 1

            old_x = next_x
            old_y = next_y

            available_moves = []
            moves = []
            print_board(old_x, old_y)

            if win_counter == board_x * board_y:
                print("What a great tour! Congratulations!")
                break
            elif not available_moves:
                print("No more possible moves!")
                print("Your knight visited {} squares!".format(win_counter))
                break

        break
    except Exception as e:
        print("Invalid dimensions!")
        traceback.print_exc()
