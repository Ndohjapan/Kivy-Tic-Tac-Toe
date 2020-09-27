#! python3
global Board
Board = {'t1': ' ', 't2': ' ', 't3': ' ',
         'm1': ' ', 'm2': ' ', 'm3': ' ',
         'b1': ' ', 'b2': ' ', 'b3': ' '}


def clear_board():
    global Board
    Board = {'t1': ' ', 't2': ' ', 't3': ' ',
             'm1': ' ', 'm2': ' ', 'm3': ' ',
             'b1': ' ', 'b2': ' ', 'b3': ' '}


# To Draw the table
def Table(board):
    print(board['t1'] + '|' + board['t2'] + '|' + board['t3'])
    print('-+-+-')
    print(board['m1'] + '|' + board['m2'] + '|' + board['m3'])
    print('-+-+-')
    print(board['b1'] + '|' + board['b2'] + '|' + board['b3'])

def horizontal(board):
    cont = []
    for i in board.values():
        cont += i

    for i in range(0, 9, 3):
        if cont[i] == cont[i + 1] and cont[i] == cont[i + 2] and cont[i] != ' ':
            return 1
            break
    return 0


def vertical(board):
    cont = []
    for i in board.values():
        cont += i

    for i in range(0, 3):
        if cont[i] == cont[i + 3] and cont[i] == cont[i + 6] and cont[i] != ' ':
            return 1
            break
    return 0


def cross(board):
    cont = []
    for i in board.values():
        cont += i

    for i in range(0, 3, 2):
        if cont[i] == cont[4]:
            if i == 0 and cont[i] == cont[8] and cont[i] != ' ':
                return 1
                break
            elif i != 0 and cont[i] == cont[6] and cont[i] != ' ':
                return 1
                break
    return 0


def check(board):
    ram = [horizontal(board), vertical(board), cross(board)]
    for i in ram:
        if i == 1:
            return True
            break
    return False


def check_draw(board):
    cont = []
    for i in board.values():
        cont += i
    cont = (" " in cont)
    if cont is False:
        return False
    return True


def main(move, turn):
    if move in Board and Board[move] == " ":
        Board[move] = turn
        Table(Board)
        if check(Board):
            return 1
        elif check(Board) is False and check_draw(Board) is True:
            return -1
        elif not check_draw(Board):
            return 0
    else:
        print("wrong input or wrong position")

