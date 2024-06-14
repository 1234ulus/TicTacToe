from random import randrange

def evaluate(string):
    play = 0
    for i in range(0, 20):
        if string[i:i + 3] == "xxx":
            print('You win!')
            play = 1
        elif string[i:i + 3] == "ooo":
            print('I win')
            play = 1
        else:
            i += 1
    if play < 1:
        if string.find("-") > 0:
            print('Time for next move')
        else:
            print('Nobody won')
    return play

def move(board, mark, position):
    p = int(position)
    newboard = []
    if board[p] == "-":
        if mark == "x":
            newboard = board[0:p] + board[p].replace("-", "x") + board[(p+1):20]
        elif mark == "o":
            newboard = board[0:p] + board[p].replace("-", "o") + board[(p+1):20]
    else:
        print('Position occupied, loss of move')
        newboard = board
    return newboard
def player_move (board):
    print("Where you want to put your X ?")
    pos = int(input("Number from 0 to 19: "))
    board = move(board, "x", pos)
    return board
def pc_move (board):
    pc = randrange(0, 20)
    board = move(board, "o", pc)
    return board
def tictactoe_1d():
    board = "--------------------"
    print("Time to play. You play with X, my with O. Your turn. Good luck!")
    print(f"Our board has 20 spaces and now looks like: {board}")
    board = player_move(board)
    board = pc_move(board)
    p = evaluate(board)
    while p == 0:
        print(f"Our board now looks like: {board}")
        board = player_move(board)
        p=evaluate(board)
        if p == 0:
            board = pc_move(board)
            p = evaluate(board)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tictactoe_1d()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
