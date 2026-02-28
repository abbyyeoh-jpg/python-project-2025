import random

def display_board (board):
    for row in board:
        print (row)
    print ()

def enter_move (board):
    while True:
        try:
            user_input = int(input("enter 1-9:"))

            if user_input in range (1, 10):
                row = (user_input - 1) //3
                col = (user_input - 1) % 3

                if isinstance (board[row][col], int):
                    board [row][col] = "O"
                    break
                else:
                    print("Square already taken.")
                    
            else:
                print("Please enter 1-9 only")

        except ValueError:
            print ("Invalid input, enter number.")

def make_list_of_free_fields (board):
    free_field = []

    for row in range (3):
        for col in range (3):
            if isinstance (board [row][col], int):
                free_field.append ((row, col))

    return free_field

def draw_move (board):
    free_field = make_list_of_free_fields (board)

    def find_winning_move (sign):
        for row, col in free_field:
            board[row][col] = sign
            if victory_for (board, sign):
                board[row][col] = (row *3 + col +1)
                return (row, col)
            board[row][col] = (row *3 + col +1)
        return None

    move = find_winning_move("X")
    if move:
        row, col = move
        board[row][col] = "X"
        return

    move = find_winning_move("O")
    if move:
        row, col = move
        board[row][col] = "X"
        return
    
    if isinstance (board [1][1], int):
        board[1][1]= "X"
        return
    
    corner = [(0,0), (0,2), (2,0), (2,2)]
    available_corner = [(row, col) for (row, col) in corner if isinstance (board [row][col], int)]
    if available_corner:
        row, col =random.choice (available_corner)
        board [row][col] = "X"
        return
              
    row, col = random.choice (free_field)
    board [row][col] = "X"

def victory_for (board, sign):
    for row in range (3):
        if board [row][0] == sign and board [row][1] == sign and board [row][2] == sign:
            return True
        
    for col in range (3):
        if board [0][col] == sign and board [1][col] == sign and board [2][col] == sign:
            return True
        
    if board [0][0] == sign and board [1][1] == sign and board [2][2] == sign:
        return True
    
    if board [0][2] == sign and board[1][1] == sign and board [2][0] == sign:
        return True
    
    return False

board =[
        [1,2,3],
        [4,5,6],
        [7,8,9]
       ]

display_board (board)

while True:
    
    enter_move(board)
    display_board (board)
        
    if victory_for (board, "O"):
        print ("Congratulation, You are winner.")
        break
        
    if not make_list_of_free_fields(board):
        print ("It is draw")
        break
        
    
    draw_move (board)
    display_board (board)

    if victory_for (board, "X"):
        print ("Computer is winner")
        break

    if not make_list_of_free_fields(board):
        print ("It is draw")
        break
                                
