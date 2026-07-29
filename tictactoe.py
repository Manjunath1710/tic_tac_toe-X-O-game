board=[" " for i in range(9)]
def game_board():
    print()
    for i in range(0, 9, 3):
        print(
            board[i] if board[i] != " " else i, "|",
            board[i+1] if board[i+1] != " " else i+1, "|",
            board[i+2] if board[i+2] != " " else i+2
        )
        if i < 6:
            print("--+---+--")
    print()

def winner(player):
    win_positions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for pos in win_positions:
        if board[pos[0]]==board[pos[1]]==board[pos[2]]==player:
            return True
    return False

def draw():
    return " " not in board

player="X"

while True:
    game_board()
    try:
        move=int(input("Enter position:"))
    except ValueError:
        print( "Please enter a number between 0 and 8.")
        continue
    if move<0 or move>8:
        print("Inavlid Entry!")
        continue

    if board[move]!=" ":
        print("Position already taken please enter another position")
        continue

    board[move]=player

    if winner(player):
        game_board()
        print(player,"is winner")
        break

    if draw():
        game_board()
        print("Its a draw!")
        break
    player = "O" if player == "X" else "X"

