from random import randrange

def evaluate(string):
    play = 0
    if "xxx" in string:
        print('You win!')
        play = 1
    elif "ooo" in string:
        print('I win')
        play = 1
    elif "-" not in string:
        print('Nobody won')
        play = 1
    return play

def move(board, mark, position):
    p = int(position)
    newboard = []
    if board[p] == "-":
        if mark == "x":
            newboard = board[0:p] + "x" + board[(p+1):]
        elif mark == "o":
            newboard = board[0:p] + "o" + board[(p+1):]
    else:
        print('Position occupied, loss of move')
        newboard = board
    return newboard
def player_move (board):
    print("Where you want to put your X ?")
    pos = int(input("Number from 0 to 19: "))
    if pos not in range (0,20):
        print("Position not in the range")
        print('Loss of move')
        return(board)
    else:
        board = move(board, "x", pos)
        return board     

def pc_move (board):
    pc = randrange(0, 20)
    print("My move is:", pc)
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
