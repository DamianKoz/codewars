import numpy as np
import codewars_test as test


def knight(p1, p2):
    QUEUE = []
    MOVES = 1
    start = turn_notation_into_coordinates(p1)
    end = turn_notation_into_coordinates(p2)

    board = np.zeros((8, 8))

    QUEUE.append(start)

    # get_possible_moves(start)

    board[start[0]][start[1]] = 1
    board[end[0]][end[1]] = 2

    while QUEUE:
        num_of_possibilities = len(QUEUE)

        for i in range(num_of_possibilities):
            move = QUEUE.pop(0)
            board[move[0]][move[1]] = MOVES
            moves = get_possible_moves(move)
            for move in moves:
                QUEUE.append(move)

        if end in QUEUE:
            print(f"FINISHED IN {MOVES} moves")
            print(board)
            break
        MOVES += 1
    return MOVES


def turn_notation_into_coordinates(notation):
    letter = notation[0]
    x = turn_letter_into_num(letter)
    y = 9 - int(notation[1])
    return [y - 1, x]


def turn_letter_into_num(position):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for i in range(len(letters)):
        if letters[i] == position:
            return i


def get_possible_moves(position):
    x, y = position[0], position[1]
    knight_moves = [
        (2, 1),
        (1, 2),
        (-1, 2),
        (-2, 1),
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1),
    ]
    moves = [[x + xd, y + yd] for xd, yd in knight_moves]
    moves = [[x, y] for x, y in moves if x >= 0 and x < 8 and y >= 0 and y < 8]
    return moves


arr = [
    ["a1", "c1", 2],
    ["a1", "f1", 3],
    ["a1", "f3", 3],
    ["a1", "f4", 4],
    ["f2", "a8", 5],
    ["a1", "f7", 5],
]
for x in arr:
    z = knight(x[0], x[1])
    test.expect(z == x[2], "{} to {}: expected {}, got {}".format(x[0], x[1], x[2], z))
