board = [
    [0,9,0,5,0,0,0,0,0],
    [2,0,1,0,0,0,0,4,5],
    [0,0,0,0,2,6,0,0,0],
    [3,4,0,0,0,0,7,0,0],
    [0,0,9,8,0,7,2,0,0],
    [0,0,6,0,0,0,0,1,8],
    [0,0,0,9,4,0,0,0,0],
    [1,8,0,0,0,0,4,0,3],
    [0,0,0,0,0,1,0,2,0]
]
 
def solved(board):
     
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, column = find
     
    for i in range(1, 10):
        if valid(board, i, (row, column)):
            board[row][column] = i
             
            if solved(board):
                return True
             
            board[row][column] = 0
     
    return False       
  
def valid(board, number, positions):
     
    #check rows
    for i in range(len(board[0])):
        if board[positions[0]][i] == number and positions[1] != i:
            return False
    
    #check columns
    for i in range(len(board)):
        if board[i][positions[1]] == number and positions[0] != i:
            return False    
     
    #check box
    box_x = positions[1] // 3
    box_y = positions[0] // 3
     
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == number and (i, j) != positions:
                return False
     
    return True    
     
def printBoard(board):
     
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("-----------------------")
             
        for j in range(len(board[0])):
            if j%3 == 0 and j != 0:
                print(" | ", end="")
                     
            if j == 8:
                print(board[i][j])
                     
            else:
                print(str(board[i][j]) + " ", end="") 
                              
 
def findEmpty(board):
     
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return(i, j)
     
    return None  

print("This is unsolved sudoku...")                   
printBoard(board)  
solved(board)
print("*****************************") 
print("solved above sudoku...") 
printBoard(board) 